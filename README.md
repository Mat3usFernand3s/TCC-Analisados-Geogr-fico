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
* `main_gui_universal.exe`: Aplicativo executável compilado (*standalone*). O usuário final **não precisa** ter o Python ou qualquer biblioteca instalada em seu computador para rodar o sistema.
* `coordenadas_brasil.csv`: Base de dados geográfica contendo a latitude e longitude dos 5.570 municípios brasileiros, necessária para a geocodificação offline.
* `main_gui_universal.py`: Código-fonte original em Python mantido no repositório para fins de consulta, transparência e auditoria lógica.
* `TCC - Mateus Fernandes dos Santos.pdf`: Artigo científico completo detalhando a fundamentação teórica, metodologia arquitetural e discussões dos resultados.
* `Apresentação TCC v5.pptx`: Material de apoio visual utilizado na defesa para a banca de avaliação.

## 🚀 Como Executar o Projeto

Para rodar o sistema de geoinformação, **não é necessário instalar nenhuma dependência ou utilizar o terminal de comando**. Todo o ecossistema de código foi empacotado para ser executado de maneira direta e visual.

### Passo a passo para execução:

1. Baixe os arquivos **`main_gui_universal.exe`** e **`coordenadas_brasil.csv`** deste repositório (ou clone o repositório usando o comando abaixo):
``bash
git clone [https://github.com/Mat3usFernand3s/TCC-Analisados-Geogr-fico.git](https://github.com/Mat3usFernand3s/TCC-Analisados-Geogr-fico.git)``

1. Certifique-se de que o arquivo coordenadas_brasil.csv esteja localizado na mesma pasta/diretório do executável main_gui_universal.exe.

2. Dê um duplo clique no arquivo main_gui_universal.exe para iniciar o programa.

3. Na interface gráfica que se abrirá na sua tela:

  Clique em "Selecionar Arquivo CSV" e importe qualquer planilha de dados abertos municipal (ex: dados de transferências do Portal da Transparência).

  Nos menus suspensos (Comboboxes), selecione quais colunas do seu arquivo representam o Município, o Valor e a UF.

4. Clique no botão verde "GERAR MAPA ANALÍTICO".

O sistema processará as informações instantaneamente de forma offline e abrirá o dashboard analítico com o mapa interativo diretamente no seu navegador de internet padrão.

👨‍💻 Autor
Mateus Fernandes dos Santos Bacharelado em Sistemas de Informação - UDESC
