import time
import random

colecao = ["Computador", "Tela", "Teclado"]
tempo = 0

for i in range (0, 10):
    palavra = random.choice(colecao)
    digitado = ""

    inicio = time.time()
    while digitado != palavra:
        digitado = input(f"Digite a {i +1} palavra {palavra}: ")
    fim = time.time()
    tempo = tempo + (fim - inicio)
print(f"Seu tempo médio por palavra foi {tempo/10} segundos.")


