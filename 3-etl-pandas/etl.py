import pandas as pd

df = pd.read_csv("dados.csv")
df = df.dropna()
df["valor_total"] = df["quantidade"] * df["preco"]
df_filtrado = df[df["valor_total"] > 100]
df_filtrado.to_csv("resultado.csv", index=False)
