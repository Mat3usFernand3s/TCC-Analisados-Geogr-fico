import pandas as pd
import folium
import os
import webbrowser
import unicodedata
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# --- CONFIGURAÇÕES ---
ARQUIVO_COORD_BR = 'coordenadas_brasil.csv'
MAPA_SAIDA = 'dashboard_analitico.html'

def remover_acentos(texto):
    if not isinstance(texto, str) or pd.isna(texto): return ""
    return "".join(c for c in unicodedata.normalize('NFD', str(texto))
                   if unicodedata.category(c) != 'Mn').upper().strip()

# --- MOTOR DE PROCESSAMENTO ---
def gerar_dashboard(caminho_csv, col_mun, col_val, col_uf, uf_alvo):
    try:
        if not os.path.exists(ARQUIVO_COORD_BR):
            return False, f"Arquivo '{ARQUIVO_COORD_BR}' não encontrado!"

        df_coords = pd.read_csv(ARQUIVO_COORD_BR)
        df_coords['mun_clean'] = df_coords['municipio'].apply(remover_acentos).astype(str)
        
        try:
            df_user = pd.read_csv(caminho_csv, sep=';', encoding='latin1', low_memory=False)
        except:
            df_user = pd.read_csv(caminho_csv, sep=';', encoding='utf-8', low_memory=False)

        # Filtro de UF
        if uf_alvo != "TODOS":
            df_user = df_user[df_user[col_uf].astype(str).str.upper() == uf_alvo.upper()]
        
        if df_user.empty:
            return False, f"Nenhum dado encontrado para a UF: {uf_alvo}"

        # Tratamento de Valores
        df_user = df_user.dropna(subset=[col_mun])
        df_user['valor_num'] = (
            df_user[col_val].astype(str)
            .str.replace(r'[^\d,]', '', regex=True)
            .str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
        )
        df_user['valor_num'] = pd.to_numeric(df_user['valor_num'], errors='coerce')
        
        # Agrupamento e Top 20
        df_resumo = df_user.groupby(col_mun, as_index=False)['valor_num'].sum()
        df_top20 = df_resumo.nlargest(20, 'valor_num').copy()
        
        df_top20['mun_clean'] = df_top20[col_mun].apply(remover_acentos).astype(str)
        df_final = pd.merge(df_top20, df_coords, on='mun_clean', how='inner')

        # Configuração do Mapa
        centro = [df_final['latitude'].mean(), df_final['longitude'].mean()]
        mapa = folium.Map(location=centro, zoom_start=6 if uf_alvo != "TODOS" else 4, tiles=None)
        
        folium.TileLayer(tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google', name='Satélite').add_to(mapa)
        folium.TileLayer(name='Ruas (OSM)').add_to(mapa)

        # Injeção de Dashboard HTML
        itens_ranking = ""
        for i, row in df_final.iterrows():
            v_fmt = f"R$ {row['valor_num']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            itens_ranking += f'<div style="display:flex; justify-content:space-between; font-size:12px; border-bottom:1px solid #eee; padding:3px 0;">' \
                             f'<b>#{i+1}</b> <span style="flex-grow:1; margin-left:8px;">{row[col_mun]}</span> <b>{v_fmt}</b></div>'

        dashboard_html = f'''
        <div style="position:fixed; top:10px; left:50px; z-index:9999; background:white; padding:12px; border:2px solid #ccc; border-radius:8px; font-family:sans-serif; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
            <b style="color:#2c3e50;">Variável: {col_val}</b> | <b>UF: {uf_alvo}</b>
        </div>
        <div style="position:fixed; top:100px; right:10px; width:300px; z-index:9999; background:rgba(255,255,255,0.95); padding:15px; border-radius:10px; border:2px solid #ccc; font-family:sans-serif; max-height:70vh; overflow-y:auto; box-shadow: 2px 2px 10px rgba(0,0,0,0.2);">
            <h4 style="margin:0 0 10px 0; text-align:center; border-bottom: 2px solid #333;">RANKING TOP 20</h4>
            {itens_ranking}
        </div>
        '''
        mapa.get_root().html.add_child(folium.Element(dashboard_html))

        for i, row in df_final.iterrows():
            folium.Marker([row['latitude'], row['longitude']], 
                          tooltip=f"{row[col_mun]}: {row['valor_num']}",
                          icon=folium.Icon(color="orange" if i < 3 else "green")).add_to(mapa)

        folium.LayerControl(collapsed=False).add_to(mapa)
        mapa.save(MAPA_SAIDA)
        webbrowser.open(f"file://{os.path.abspath(MAPA_SAIDA)}")
        return True, "Análise gerada com sucesso!"
    except Exception as e:
        return False, str(e)

# --- INTERFACE GRÁFICA ---
class AppModerno:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador Geográfico")
        self.root.geometry("600x680")
        self.root.configure(bg="#F4F7F6") # Cinza claro/frio para harmonia

        # Cores e Estilos
        self.bg_color = "#F4F7F6"
        self.primary_color = "#2C3E50" # Azul ardósia
        self.accent_color = "#27AE60"  # Verde esmeralda
        
        # Título
        tk.Label(root, text="DASHBOARD DE DADOS GEOGRÁFICOS", font=("Segoe UI", 16, "bold"), bg=self.bg_color, fg=self.primary_color).pack(pady=(30, 20))

        # Card de Upload
        self.card_upload = tk.Frame(root, bg="white", padx=20, pady=20, highlightbackground="#DCDDE1", highlightthickness=1)
        self.card_upload.pack(padx=40, fill="x")

        tk.Label(self.card_upload, text="1. ORIGEM DOS DADOS", font=("Segoe UI", 10, "bold"), bg="white", fg=self.primary_color).pack(anchor="w")
        self.btn_load = tk.Button(self.card_upload, text="📁 Selecionar Arquivo CSV", command=self.carregar_csv, font=("Segoe UI", 10), bg="#ECF0F1", relief="flat", height=2, cursor="hand2")
        self.btn_load.pack(pady=10, fill="x")
        self.lbl_file = tk.Label(self.card_upload, text="Nenhum arquivo selecionado", font=("Segoe UI", 8), bg="white", fg="#95A5A6")
        self.lbl_file.pack()

        # Card de Configuração
        self.card_config = tk.Frame(root, bg="white", padx=20, pady=20, highlightbackground="#DCDDE1", highlightthickness=1)
        self.card_config.pack(padx=40, pady=20, fill="x")

        tk.Label(self.card_config, text="2. PARÂMETROS DE ANÁLISE", font=("Segoe UI", 10, "bold"), bg="white", fg=self.primary_color).pack(anchor="w", pady=(0, 10))

        # Comboboxes
        self.criar_label_combo(self.card_config, "Coluna de Município:", "cb_mun")
        self.criar_label_combo(self.card_config, "Coluna de Valor:", "cb_val")
        self.criar_label_combo(self.card_config, "Coluna de UF:", "cb_uf_col")
        
        # Filtro de UF
        tk.Label(self.card_config, text="Recorte Geográfico:", font=("Segoe UI", 9, "bold"), bg="white", fg=self.primary_color).pack(anchor="w", pady=(10, 5))
        self.cb_uf_alvo = ttk.Combobox(self.card_config, state="disabled")
        self.cb_uf_alvo.pack(fill="x")

        # Botão Ação
        self.btn_gerar = tk.Button(root, text="GERAR MAPA ANALÍTICO", command=self.gerar, state="disabled", font=("Segoe UI", 12, "bold"), bg=self.accent_color, fg="white", relief="flat", height=2, cursor="hand2")
        self.btn_gerar.pack(pady=20, padx=40, fill="x")

        self.caminho_csv = ""

    def criar_label_combo(self, parent, label_text, attr_name):
        tk.Label(parent, text=label_text, font=("Segoe UI", 9), bg="white", fg="#555").pack(anchor="w")
        cb = ttk.Combobox(parent, state="disabled")
        cb.pack(fill="x", pady=(0, 10))
        setattr(self, attr_name, cb)
        if attr_name == "cb_uf_col":
            cb.bind("<<ComboboxSelected>>", self.atualizar_lista_ufs)

    def carregar_csv(self):
        file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file:
            self.caminho_csv = file
            try:
                df = pd.read_csv(file, sep=';', encoding='latin1', nrows=0)
            except:
                df = pd.read_csv(file, sep=';', encoding='utf-8', nrows=0)
            
            cols = df.columns.tolist()
            for cb_name in ["cb_mun", "cb_val", "cb_uf_col"]:
                cb = getattr(self, cb_name)
                cb['values'] = cols
                cb.config(state="readonly")
            self.lbl_file.config(text=os.path.basename(file), fg=self.primary_color)

    def atualizar_lista_ufs(self, event):
        col_uf = self.cb_uf_col.get()
        try:
            df = pd.read_csv(self.caminho_csv, sep=';', encoding='latin1', usecols=[col_uf])
        except:
            df = pd.read_csv(self.caminho_csv, sep=';', encoding='utf-8', usecols=[col_uf])
        
        ufs = sorted(df[col_uf].dropna().unique().astype(str).tolist())
        self.cb_uf_alvo['values'] = ["TODOS"] + ufs
        self.cb_uf_alvo.set("TODOS")
        self.cb_uf_alvo.config(state="readonly")
        self.btn_gerar.config(state="normal")

    def gerar(self):
        m, v, cu, au = self.cb_mun.get(), self.cb_val.get(), self.cb_uf_col.get(), self.cb_uf_alvo.get()
        if not all([m, v, cu, au]): return
        
        sucesso, msg = gerar_dashboard(self.caminho_csv, m, v, cu, au)
        if not sucesso: messagebox.showerror("Erro", msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppModerno(root)
    root.mainloop()