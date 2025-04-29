
import streamlit as st
import pandas as pd
import os

# ─── CONFIGURAÇÃO DA PÁGINA ────────────────────────────────────────
st.set_page_config(
    page_title="ABC Habitação",
    page_icon="logo_abc.png",  # LOGO oficial como ícone
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── LOGO E TÍTULO ────────────────────────────────────────────────
st.image("logo_abc.png", width=200)
st.title("ABC Habitação - Sistema de Ofícios e Relatórios")

# ─── CARREGAMENTO DOS DADOS ───────────────────────────────────────
st.subheader("Relatório de Envios")

if os.path.exists("relatorio_envio.csv"):
    df = pd.read_csv("relatorio_envio.csv")
    st.dataframe(df)

    filiado = st.text_input("Buscar por Filiado:")

    if filiado:
        resultados = df[df["Filiado"].str.contains(filiado, case=False, na=False)]
        st.dataframe(resultados)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Relatório Completo",
        data=csv,
        file_name='relatorio_envio.csv',
        mime='text/csv',
    )
else:
    st.warning("Nenhum relatório encontrado ainda.")
