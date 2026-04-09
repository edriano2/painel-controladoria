import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar dados
df = pd.read_excel("base_supermercado.xlsx")

st.set_page_config(layout="wide")

st.title("📊 Painel de Controladoria - Supermercados")

# Filtros
loja = st.selectbox("Selecione a Loja", ["Todas"] + list(df["Loja"].unique()))

if loja != "Todas":
    df = df[df["Loja"] == loja]

# ========================
# RESUMO GERAL
# ========================
st.header("📌 Resumo Geral")

faturamento = df["Faturamento"].sum()
lucro = df["Lucro"].sum()
margem = (lucro / faturamento) * 100
clientes = df["Clientes"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Faturamento", f"R$ {faturamento:,.0f}")
col2.metric("Lucro", f"R$ {lucro:,.0f}")
col3.metric("Margem", f"{margem:.2f}%")
col4.metric("Clientes", f"{clientes:,}")

# ========================
# COMPARATIVO LOJAS
# ========================
st.header("🏪 Comparativo entre Lojas")

df_lojas = df.groupby("Loja")[["Faturamento", "Lucro"]].sum().reset_index()

fig_lojas = px.bar(df_lojas, x="Loja", y="Faturamento", title="Faturamento por Loja")
st.plotly_chart(fig_lojas, use_container_width=True)

# ========================
# VENDAS E CLIENTES
# ========================
st.header("🛒 Vendas e Clientes")

fig_vendas = px.line(df, x="Data", y="Faturamento", title="Evolução de Vendas")
st.plotly_chart(fig_vendas, use_container_width=True)

# ========================
# CUSTOS
# ========================
st.header("💸 Custos")

df_custos = df[["Faturamento", "Custo"]].sum()
fig_custos = px.pie(
    names=["Custo", "Lucro"],
    values=[df_custos["Custo"], df_custos["Faturamento"] - df_custos["Custo"]],
    title="Distribuição Custo vs Lucro"
)
st.plotly_chart(fig_custos)

# ========================
# ESTOQUE
# ========================
st.header("📦 Estoque")

estoque_total = df["Estoque"].sum()
st.metric("Valor em Estoque", f"R$ {estoque_total:,.0f}")

# ========================
# MARGEM
# ========================
st.header("📊 Margem por Loja")

df_margem = df.groupby("Loja")[["Faturamento", "Lucro"]].sum()
df_margem["Margem %"] = (df_margem["Lucro"] / df_margem["Faturamento"]) * 100

st.dataframe(df_margem)

# ========================
# ALERTAS
# ========================
st.header("⚠️ Alertas")

if margem < 10:
    st.error("Margem baixa! Verificar custos.")

if df["Estoque"].mean() > 120000:
    st.warning("Estoque elevado! Possível dinheiro parado.")

if faturamento < 1000000:
    st.info("Faturamento abaixo do esperado.")
    from utils.dre import gerar_dre

st.subheader("📊 DRE (Resultado)")

dre = gerar_dre(df)

for k, v in dre.items():
    st.write(f"{k}: R$ {v:,.0f}")
    from utils.estoque import analise_estoque

st.subheader("📦 Estoque Inteligente")

estoque_total, giro, parado, ruptura = analise_estoque(df)

st.metric("Estoque Total", f"R$ {estoque_total:,.0f}")
st.metric("Giro Médio", f"{giro:.2f}")

if len(parado) > 0:
    st.warning("Existem produtos com baixo giro (parados).")

if len(ruptura) > 0:
    st.error("Possível ruptura em produtos de alta venda.")