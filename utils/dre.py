def gerar_dre(df):
    receita = df["Faturamento"].sum()
    custo = df["Custo"].sum()
    lucro_bruto = receita - custo

    despesas_operacionais = receita * 0.15  # simulação
    lucro_operacional = lucro_bruto - despesas_operacionais

    impostos = receita * 0.08
    lucro_liquido = lucro_operacional - impostos

    dre = {
        "Receita": receita,
        "Custo": custo,
        "Lucro Bruto": lucro_bruto,
        "Despesas Operacionais": despesas_operacionais,
        "Lucro Operacional": lucro_operacional,
        "Impostos": impostos,
        "Lucro Líquido": lucro_liquido
    }

    return dre