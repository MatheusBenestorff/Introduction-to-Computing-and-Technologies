valores= []
i=1
while(i<=10):
    valor=int(input(f"Digite o valor {i}/10: "))
    valores.append(valor)
    i=i+1

modificada= []

for valor in valores:
    if valor < 0:
        modificada.append(abs(valor))
    else:
        modificada.append(valor)

print("Lista modificada:")
print(modificada)