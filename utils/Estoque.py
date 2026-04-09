def analise_estoque(df):
    df["Giro"] = df["Faturamento"] / (df["Custo"] + 1)

    estoque_total = df["Custo"].sum()
    giro_medio = df["Giro"].mean()

    alerta_parado = df[df["Giro"] < 1]
    alerta_ruptura = df[df["Faturamento"] > 15000]

    return estoque_total, giro_medio, alerta_parado, alerta_ruptura