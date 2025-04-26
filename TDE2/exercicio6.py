precoNormal =float(input("Digite o valor do produto: "))

print("")
print("---Condições de pagamento---")
print("(1) à vista em dinheiro/cheque.")
print("(2) à vista no cartão de crédito.")
print("(3) em até 2x no cartão de crédito.")
print("(4) 3x ou mais no cartão de crédito.")

condicao =int(input("Digite a condição de pagamento: "))

print("")

if (condicao ==1):
    precoFinal = precoNormal - (precoNormal *0.1)
    print(f"Valor a ser pago: {precoFinal} reais")
elif (condicao ==2):
    precoFinal = precoNormal - (precoNormal *0.05)    
    print(f"Valor a ser pago: {precoFinal} reais")
elif (condicao ==3):  
    print(f"Valor a ser pago: {precoNormal} reais")
elif (condicao ==4):
    precoFinal = precoNormal + (precoNormal *0.1)    
    print(f"Valor a ser pago: {precoFinal} reais")
else:
    print("Valor de condição inválido, digite um número entre 1 e 4.")              