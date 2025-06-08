import pandas as pd

dados = pd.read_csv("Tabela.csv")

print(dados,
      )

dados.loc[len(dados)] = 3500

print(dados)

dados.to_csv("Tabela.csv", index = False)