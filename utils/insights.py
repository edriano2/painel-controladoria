def gerar_insights(df):
    insights = []

    faturamento = df["Faturamento"].sum()
    lucro = df["Lucro"].sum()
    margem = (lucro / faturamento) * 100

    if margem < 15:
        insights.append("Margem baixa. Avaliar preços ou custos.")

    loja_top = df.groupby("Loja")["Faturamento"].sum().idxmax()
    insights.append(f"{loja_top} é a loja com maior faturamento.")

    categoria_ruim = df.groupby("Categoria")["Lucro"].sum().idxmin()
    insights.append(f"{categoria_ruim} tem menor lucratividade.")

    return insights
from utils.insights import gerar_insights

st.subheader("🧠 Análise Automática")

insights = gerar_insights(df)

for i in insights:
    st.write(f"- {i}")