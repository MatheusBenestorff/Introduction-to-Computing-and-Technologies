valores= []
i=1
while(i<=10):
    valor=int(input(f"Digite o valor {i}/10: "))
    valores.append(valor)
    i=i+1

valores.reverse()

print("Lista digitada: ")
print(f"{valores}")
