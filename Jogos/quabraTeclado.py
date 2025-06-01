import time
import random

colecao = ["Computador", "Tela", "Teclado"]
digitado = ""
palavra = random.choice(colecao)

inicio = time.time()


while digitado != palavra:
    digitado = input(f"Digite a palavra {palavra}: ")

fim = time.time()
print(f"Digitou a palavra correta!!! Você levou {fim-inicio} segundos.")