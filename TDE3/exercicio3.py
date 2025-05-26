valores= []
i=1
while(i<=10):
    valor=int(input(f"Digite o valor {i}/10: "))
    valores.append(valor)
    i=i+1

pares= []
impares= []

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("Números pares:")
print(pares)
print("Números ímpares:")
print(impares)
