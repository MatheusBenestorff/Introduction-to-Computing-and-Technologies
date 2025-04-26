valorCasa =int(input("Digite o valor da casa: "))
salario =int(input("Digite o salário do comprador: "))
anos =int(input("Digite a quantidade de anos em que o comprador pretende pagar a casa: "))

valorPrestacao = valorCasa / anos

print(f"Valor da Casa: {valorCasa} reais")
print(f"Salário: {salario} reais")
print(f"Anos: {anos}")

if valorPrestacao <= (salario *0.3):
    print("Empréstimo Aprovado!")
else:
    print("Empréstimo Negado.")    
