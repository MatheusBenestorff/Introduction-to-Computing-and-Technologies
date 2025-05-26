valores= []
i=1
while(i<=10):
    valor = int(input(f"Digite o valor {i}/10: "))
    valores.append(valor)
    i=i+1

posicoes= []

for posicao, valor in enumerate(valores):
    if valor < 0:
        posicoes.append(posicao)

print("Posições da lista que possuem números menores que zero:")
print(posicoes)