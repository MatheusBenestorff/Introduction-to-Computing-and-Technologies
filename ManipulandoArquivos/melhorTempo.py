import time
import random
import pandas as pd

colecao = ["Computador", "Tela", "Teclado"]
digitado = ""
palavra = random.choice(colecao)

inicio = time.time()

while digitado != palavra:
    digitado = input(f"Digite a palavra {palavra}: ")

fim = time.time()
tempoAtual = fim - inicio
print(f"Digitou a palavra correta!!! Você levou {tempoAtual} segundos.")


dados= pd.read_csv("MelhorTempo.csv")
melhorTempo = dados['Tempos'].values[-1]

if tempoAtual < melhorTempo:
    dados.loc[len(dados)] = tempoAtual
    dados.to_csv("MelhorTempo.csv", index = False)