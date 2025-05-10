import random
import time

personagem = "Meu Personagem"
forca = 1
forcaop = 0
ouro = 0

time.sleep(1)
print("Primeiro Oponente:")
time.sleep(1)
d1 = random.randrange(1, 7)
do = random.randrange(1, 7)
print("-----------------------------------------------")

time.sleep(1)
print(f" \t\t Personagem  vs  Oponente")
print(f"Força:  \t {forca}  \t vs  \t {0}")
time.sleep(1)
print(f"Ataque:  \t {forca + d1}  \t vs  \t {forcaop + do}")
print("-----------------------------------------------")
time.sleep(1)

if (forca + d1 >= forcaop + do):
    ganho = random.randint(1, 10)
    print("Você venceu!")
    time.sleep(1)
    print(f"Você tinha {ouro} moedas de ouro.")
    time.sleep(1)
    print(f"Recompensa de vitória: {ganho} moedas de ouro")
    ouro = ouro + ganho
    print(f"Saldo: {ouro} moedas de ouro")
    print("-----------------------------------------------")
else:
    print("Game Over.")
    exit(0)

time.sleep(1)
if (ouro >= 5):
    print("Quer comprar 1 ponto de força por 5 moedas?")
    upgrade = input("[S]im / [N]ão: ")
    if (upgrade == "S"):
        time.sleep(1)
        print("-----------------------------------------------")
        forca += 1
        ouro -= 5
        print("Personagem upado!")
        print(f"Força: {forca}")
        print(f"Saldo: {ouro} moedas de ouro")
