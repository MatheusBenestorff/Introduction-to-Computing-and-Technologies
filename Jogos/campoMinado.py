from random import*
lista= []
for a in range(1,5):
    for b in range(1,5):
        lista.append([randint(0,4)])

linha=-1
coluna=-1
rodada=1

while(True):
    print(f"Rodada: {rodada}")
    print("-"*30)
    lista[(((linha-1)*4) +coluna)-1]
    for a in range(1,5):
        for b in range(1,5):
            if lista[(((a-1)*4) +b)-1] == [-1]:
                print(f"[X]", end="")
            else:
                print(f"[ ]", end="")
        print("")
    linha=int(input("Digite a Linha (1 a 4): "))
    coluna=int(input("Digite a Coluna (1 a 4): "))
    valor_posicao=lista[(((linha-1)*4) +coluna)-1]
    if valor_posicao== [0]:
        print("Uma bomba explodiu! Você Morreu!")
        break
    elif valor_posicao== [-1]:
        print("Você já checou este local!")
    else:
        print("Não havia bomba! Você está seguro!")
        lista[(((linha-1)*4) +coluna)-1] = [-1]
        rodada+=1

print(f"Você sobreviveu até a rodada: {rodada}")