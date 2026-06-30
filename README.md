# Analisador Geográfico: Transparência Pública 🗺️📊

[![Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)]()
[![Folium](https://img.shields.io/badge/Folium-Mapping-green.svg)](https://python-visualization.github.io/folium/)
[![Status](https://img.shields.io/badge/Status-Concluído-success.svg)]()

Repositório destinado ao Trabalho de Conclusão de Curso (TCC) em Sistemas de Informação pela Universidade do Estado de Santa Catarina (UDESC).

Este projeto é um protótipo funcional de um Sistema de Informações Geográficas (SIG) para visualização e análise interativa de dados públicos referentes à transferência de recursos aos municípios brasileiros.

## 🎯 Objetivo
Transformar dados brutos governamentais (frequentemente planilhas CSV com milhares de linhas) em painéis analíticos geográficos (dashboards). A ferramenta visa promover a transparência e facilitar o controle social, abstraindo a complexidade técnica através de uma interface visual intuitiva e geocodificação estática 100% offline.

## ✨ Funcionalidades
* **Ingestão Dinâmica:** Interface gráfica amigável que permite ao usuário carregar qualquer arquivo municipal em formato CSV e mapear as colunas (Município, Valor e UF) em tempo real, sem depender de layouts rígidos.
* **Geocodificação Offline:** Utilização de uma base estática do IBGE para cruzamento espacial, eliminando latência de APIs externas e garantindo privacidade e velocidade.
* **Tratamento ETL Interno:** Limpeza financeira automática via RegEx e normalização Unicode para evitar quebras por erros de acentuação nos dados públicos.
* **Dashboard Interativo em HTML:** Geração automática de um mapa web (Folium/Leaflet) contendo:
  * Marcadores lógicos de concentração financeira.
  * Filtro automático por Unidade Federativa (UF) com auto-zoom.
  * Injeção de painel fixo com o **Ranking Top 20** dos repasses públicos.

## 📁 Estrutura do Repositório
* `coordenadas_brasil.csv`: Base de dados geográfica (latitude e longitude dos 5.570 municípios) necessária para a geocodificação offline.
* `main_gui_universal.py`: Código-fonte original em Python mantido no repositório para fins de consulta, transparência e auditoria lógica.
* `TCC - Mateus Fernandes dos Santos.pdf`: Artigo científico completo detalhando a fundamentação teórica e discussão dos resultados.
* `Apresentação TCC v5.pptx`: Material de apoio visual utilizado na defesa.
* **Releases (Lançamentos):** Contém o `main_gui_universal.exe`, o aplicativo executável compilado (*standalone*).

---

## 🚀 Como Executar o Projeto

Todo o ecossistema de código foi empacotado para ser executado de maneira direta e visual, sem a necessidade de instalar o Python ou usar o terminal.

### Passo a passo para execução (Usuário Final):

1. **Baixe o Executável:** Vá até a seção **Releases** (Lançamentos) localizada na lateral direita desta página e faça o download da versão mais recente do arquivo `main_gui_universal.exe`.
2. **Baixe a Base Geográfica:** Volte para a página inicial deste repositório, clique no arquivo `coordenadas_brasil.csv` e faça o download (ícone de download no canto superior direito do arquivo).
3. **Organize os arquivos:** Coloque o executável `main_gui_universal.exe` e o arquivo `coordenadas_brasil.csv` **exatamente na mesma pasta** no seu computador.
4. **Execute:** Dê um duplo clique no arquivo `main_gui_universal.exe`.
5. Na interface gráfica:
   * Clique em **"Selecionar Arquivo CSV"** e importe uma planilha de dados abertos municipal (ex: Portal da Transparência).
   * Selecione as colunas que representam o **Município**, o **Valor** e a **UF**.
6. Clique em **"GERAR MAPA ANALÍTICO"**. O mapa interativo se abrirá automaticamente no seu navegador.

### Para Desenvolvedores (Acesso ao Código-Fonte)
Caso deseje rodar a aplicação via código e terminal, clone o repositório e instale as dependências:
``bash
git clone [https://github.com/Mat3usFernand3s/TCC-Analisados-Geogr-fico.git](https://github.com/Mat3usFernand3s/TCC-Analisados-Geogr-fico.git)
pip install pandas folium
python main_gui_universal.py``

👨‍💻 Autor
Mateus Fernandes dos Santos
Bacharelado em Sistemas de Informação - UDESC

<img width="604" height="712" alt="Captura de tela 2026-04-14 173727" src="https://github.com/user-attachments/assets/f05c93ca-3c41-4308-8758-93620f9f6b50" />

<img width="1918" height="1027" alt="Captura de tela 2026-05-06 230453" src="https://github.com/user-attachments/assets/1690f165-0266-48cb-9a9d-58e826a0a268" />

<img width="1919" height="1029" alt="Captura de tela 2026-04-14 173909" src="https://github.com/user-attachments/assets/f2dc7c3e-8d63-4a13-9a65-470fe08443a3" />


