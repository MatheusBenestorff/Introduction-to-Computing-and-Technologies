import random
import time

pontosJG = 0
pontosPC = 0
ataqueJG = 0
ataquePC = 0

#Início
print("Batalha dos Elementos")
time.sleep(1)
print("--------------------------------------------------")


#Escolha dos elementos
print("")
print("Escolha o seu elemento!")
time.sleep(1)
print("1 - AR")
print("2 - Água")
print("3 - TERRA")
print("4 - FOGO")
print("")
elementoJG = int(input("Digite o número correspondente ao elemento: "))
elementoPC= random.randrange(1, 5)
print("")


#Lançamento dos dados
print("--------------------------------------------------")
print(("Lançamento dos dados do Jogador"))
time.sleep(1)
dado1JG= random.randrange(1, 7)
dado2JG= random.randrange(1, 7)
dado3JG= random.randrange(1, 7)

if (dado1JG > dado2JG) and (dado1JG > dado3JG):
    if dado2JG > dado3JG:
        ataqueJG = dado1JG + dado2JG
        escolhidosJG = f"{dado1JG} e {dado2JG}"
    else:
        ataqueJG = dado1JG + dado3JG
        escolhidosJG = f"{dado1JG} e {dado3JG}"
elif dado2JG > dado3JG:
    if dado1JG > dado3JG:
        ataqueJG = dado2JG + dado1JG
        escolhidosJG = f"{dado2JG} e {dado1JG}"
    else:
        ataqueJG = dado2JG + dado3JG
        escolhidosJG = f"{dado2JG} e {dado3JG}"
else:
    if dado2JG > dado1JG:
        ataqueJG = dado3JG + dado2JG
        escolhidosJG = f"{dado3JG} e {dado2JG}"
    else:
        ataqueJG = dado3JG + dado1JG
        escolhidosJG = f"{dado3JG} e {dado1JG}"

time.sleep(1)
print("")
print("Dados do Jogador:")
print(f"{dado1JG}, {dado2JG} e {dado3JG}")
print(("Dados escolhidos do Jogador: "))
print((f"{escolhidosJG}"))
print("")
print("Lançamento dos dados do PC")
time.sleep(1)
dado1PC= random.randrange(1, 7)
dado2PC= random.randrange(1, 7)
dado3PC= random.randrange(1, 7)

if (dado1PC > dado2PC) and (dado1PC > dado3PC):
    if dado2PC > dado3PC:
        ataquePC = dado1PC + dado2PC
        escolhidosPC = f"{dado1PC} e {dado2PC}"
    else:
        ataquePC = dado1PC + dado3PC
        escolhidosPC = f"{dado1PC} e {dado3PC}"
elif dado2PC > dado3PC:
    if dado1PC > dado3PC:
        ataquePC = dado2PC + dado1PC
        escolhidosPC = f"{dado2PC} e {dado1PC}"
    else:
        ataquePC = dado2PC + dado3PC
        escolhidosPC = f"{dado2PC} e {dado3PC}"
else:
    if dado2PC > dado1PC:
        ataquePC = dado3PC + dado2PC
        escolhidosPC = f"{dado3PC} e {dado2PC}"
    else:
        ataquePC = dado3PC + dado1PC
        escolhidosPC = f"{dado3PC} e {dado1PC}"

time.sleep(1)
print("")
print("Dados do PC:")
print(f"{dado1PC}, {dado2PC} e {dado3PC}")
print(("Dados escolhidos do PC: "))
print((f"{escolhidosPC}"))


#Definição da vantagem
if (elementoJG == 4 and elementoPC == 1):
    vantagem = "Fogo é super efetivo contra Ar!"
    ataqueJG = ataqueJG + 3
elif (elementoJG == 1 and elementoPC == 3):
    vantagem = "Ar é super efetivo contra Terra!"
    ataqueJG = ataqueJG + 3
elif (elementoJG == 3 and elementoPC == 2):
    vantagem = "Terra é super efetivo contra Água!"
    ataqueJG = ataqueJG + 3
elif (elementoJG == 2 and elementoPC == 4):
    vantagem = "Água é super efetivo contra Fogo!"
    ataqueJG = ataqueJG + 3
elif elementoJG == elementoPC:
    vantagem = "Os elementos são iguais, sem vantagem!"
elif (elementoJG != 1) and (elementoJG != 2) and (elementoJG != 3) and (elementoJG != 4):
    ataquePC = ataquePC
else:
    vantagem = "O jogador tomou um ataque super efetivo!"
    ataquePC = ataquePC + 3
print("--------------------------------------------------")
print("")


#Batalha
time.sleep(2)
print("========  |  ========  |      |   =========  |")
print("|         |  |         |      |       |      |")
print("|====     |  |    ==|  |======|       |      |")
print("|         |  |      |  |      |       |      |")
print("|         |  ========  |      |       |      =")
print("")
print("Inicio da batalha!")
if elementoJG == 1:
    print("O jogador escolheu Ar")
elif elementoJG == 2:
    print("O jogador escolheu Água")
elif elementoJG == 3:
    print("O jogador escolheu Terra")
elif elementoJG == 4:
    print("O jogador escolheu Fogo")
else:
    print("O jogador decidiu lutar sem um elemento!!")

time.sleep(1)
if (elementoJG == 1) or (elementoJG == 2) or (elementoJG == 3) or (elementoJG == 4):
    if elementoPC == 1:
        print("O PC escolheu Ar")
    elif elementoPC == 2:
        print("O PC escolheu Água")
    elif elementoPC == 3:
        print("O PC escolheu Terra")
    elif elementoPC == 4:
        print("O PC escolheu Fogo")
else:
    vantagem = "Batalha sem vantagens!"

time.sleep(1)
print(f"{vantagem}")
print("")

time.sleep(1)
print("JOGADOR \t  PC")
print(f"   {ataqueJG} \t\t  {ataquePC}")
print("")
time.sleep(1)
if ataqueJG > ataquePC:
    print("O Jogador ganhou a batalha!")
    print("                             / ")
    print("|       |  |  =========  ========  ========   |   ========")
    print(" |     |   |      |      |      |  |       |  |   |      |")
    print("  |   |    |      |      |      |  |=======   |   |======|")
    print("   | |     |      |      |      |  |   |      |   |      |")
    print("    V      |      |      ========  |     |    |   |      |")
elif ataqueJG == ataquePC:
    print("A Batalha terminou empatada.")
    print("")
    print("========  |          |  ========   ========  =========  ======== ")
    print("|         | |      | |  |       |  |      |      |      |        ")
    print("|======   |   |   |  |  |=======   |======|      |      |======  ")
    print("|         |    | |   |  |          |      |      |      |        ")
    print("========  |     |    |  |          |      |      |      ======== ")
else:
    print("O PC ganhou a batalha.")
    print("")
    print("=========    ========  ========   ========    ========   =========  ========")
    print("|        |   |         |       |  |       |   |      |       |      |      |")
    print("|         |  |======   |=======   |=======    |      |       |      |======|")
    print("|        |   |         |   |      |   |       |      |       |      |      |")
    print("========     ========  |     |    |     |     ========       |      |      |")

#Fim