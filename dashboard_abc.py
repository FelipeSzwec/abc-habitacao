import streamlit as st
import pandas as pd
import os

# ─── CONFIGURAÇÃO DA PÁGINA ────────────────────────────────────────
st.set_page_config(
    page_title="ABC Habitação",      # Nome da ABA do navegador
    page_icon="🏠",                  # Ícone da ABA (pode ser emoji ou imagem)
    layout="wide",                   # Tela mais aberta (wide)
    initial_sidebar_state="expanded" # Sidebar aberta
)

# ─── LOGO E TÍTULO DO PAINEL ───────────────────────────────────────
st.image("logo_abc.png", width=200)
st.title("ABC Habitação - Sistema de Ofícios e Relatórios")  # <--- Aqui mudamos o título GRANDE na tela!

# ─── CARREGAMENTO DOS DADOS ────────────────────────────────────────
st.subheader("Relatório de Envios")

# Verifica se existe o arquivo de relatórios
if os.path.exists("relatorio_envio.csv"):
    df = pd.read_csv("relatorio_envio.csv")
    st.dataframe(df)

    # Campo para buscar Filiados
    filiado = st.text_input("Buscar por Filiado:")

    if filiado:
        resultados = df[df["Filiado"].str.contains(filiado, case=False, na=False)]
        st.dataframe(resultados)

    # Botão para baixar o relatório
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Relatório Completo",
        data=csv,
        file_name='relatorio_envio.csv',
        mime='text/csv',
    )
else:
    st.warning("Nenhum relatório encontrado ainda.")
