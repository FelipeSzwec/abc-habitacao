import streamlit as st
import pandas as pd
import os
import glob

# Configuração da página
st.set_page_config(page_title="Painel de Ofícios ABC", page_icon="🏠", layout="wide")

# Título com logo
st.image("logo_abc.png", width=200)
st.title("Painel de Ofícios ABC")
st.markdown("---")

# Carrega o relatório de envios
try:
    relatorio = pd.read_csv("relatorio_envio.csv", sep=";")
except FileNotFoundError:
    st.error("Relatório não encontrado. Execute primeiro o envio dos ofícios!")
    st.stop()

# Filtros
filiados = relatorio["Filiado"].dropna().unique()
status_envios = relatorio["Status"].dropna().unique()

filiado_selecionado = st.selectbox("Selecione um filiado:", options=["Todos"] + list(filiados))
status_selecionado = st.selectbox("Selecione um status:", options=["Todos"] + list(status_envios))

# Filtra dados
dados_filtrados = relatorio.copy()

if filiado_selecionado != "Todos":
    dados_filtrados = dados_filtrados[dados_filtrados["Filiado"] == filiado_selecionado]

if status_selecionado != "Todos":
    dados_filtrados = dados_filtrados[dados_filtrados["Status"] == status_selecionado]

st.dataframe(dados_filtrados, use_container_width=True)

st.markdown("---")
st.subheader("Ofícios gerados para Download 📄")

# Listar PDFs na pasta PDFs/[Mês atual]
mes_atual = pd.Timestamp.now().month
meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

pasta_pdfs = f"PDFs/{meses[mes_atual]}"
if not os.path.exists(pasta_pdfs):
    st.warning(f"Pasta de PDFs para {meses[mes_atual]} ainda não criada.")
else:
    pdfs = glob.glob(os.path.join(pasta_pdfs, "*.pdf"))
    for pdf in pdfs:
        nome = os.path.basename(pdf)
        with open(pdf, "rb") as f:
            btn = st.download_button(label=f"📥 Baixar {nome}", data=f, file_name=nome)

