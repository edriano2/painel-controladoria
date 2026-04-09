import os

os.makedirs("data", exist_ok=True)
import pandas as pd
import numpy as np

np.random.seed(42)

lojas = ["Loja 1", "Loja 2", "Loja 3", "Loja 4", "Loja 5"]
cidades = {"Loja 1":"Cidade A","Loja 2":"Cidade A","Loja 3":"Cidade B","Loja 4":"Cidade B","Loja 5":"Cidade B"}

categorias = ["Mercearia", "Hortifruti", "Açougue", "Bebidas", "Limpeza"]

datas = pd.date_range(start="2024-01-01", end="2024-03-31")

dados = []

for data in datas:
    for loja in lojas:
        for cat in categorias:
            faturamento = np.random.randint(5000, 20000)
            custo = faturamento * np.random.uniform(0.6, 0.85)
            clientes = np.random.randint(50, 200)

            dados.append([
                data,
                loja,
                cidades[loja],
                cat,
                faturamento,
                custo,
                faturamento - custo,
                clientes,
                faturamento / clientes
            ])

df = pd.DataFrame(dados, columns=[
    "Data","Loja","Cidade","Categoria",
    "Faturamento","Custo","Lucro","Clientes","Ticket_Medio"
])

df.to_excel("data/base_supermercado.xlsx", index=False)