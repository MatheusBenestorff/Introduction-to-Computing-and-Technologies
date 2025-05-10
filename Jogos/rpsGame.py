import random
import time

pontosUs = 0
pontosOp = 0
rodada = 1

while rodada <4:

    print(f"Rodada {rodada}")
    print("-------------------------------")
    us = int(input("Digite 1 para Pedra, 2 para Papel ou 3 para Tesoura: "))
    op = random.randrange(1, 4)

    if us == 1:
        print("Usuário escolheu Pedra")
        escolhaUs = "Pedra"
    elif us == 2:
        print("Usuário escolheu Papel")
        escolhaUs = "Papel"
    elif us == 3:
        print("Usuário escolheu Tesoura")
        escolhaUs = "Tesoura"
    else:
        print("Usuário escolheu um número inválido")

    time.sleep(1)
    if op == 1:
        print("Oponente escolheu Pedra")
        escolhaOp = "Pedra"
    elif op == 2:
        print("Oponente escolheu Papel")
        escolhaOp = "Papel"
    else:
        print("Oponente escolheu Tesoura")
        escolhaOp = "Tesoura"

    time.sleep(1) 
    if (us ==1 and op == 3) or (us == 2 and op == 1) or (us == 3 and op ==2):
        print("Usuário venceu a rodada!")
        pontosUs = pontosUs + 1
    elif us == op:
        print("Empate na rodada!")
    else:
        print("Oponente venceu a rodada.")
        pontosOp = pontosOp + 1    

    print(f"Usuário = {escolhaUs} e Oponente = {escolhaOp}")
    rodada += 1
    print("")
    time.sleep(1)

time.sleep(1)
if pontosUs > pontosOp:
    print("Usuário ganhou o jogo!")
elif pontosUs == pontosOp:
    print("O jogo terminou em empate.")
else: 
    print("O oponente ganhou o jogo.")    


                   