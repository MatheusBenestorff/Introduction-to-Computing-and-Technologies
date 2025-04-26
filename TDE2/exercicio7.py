codigo =int(input("Digite o código do item: "))
quantidade =int(input("Digite a quantidade: "))

if (codigo ==100):
    preco = quantidade *10
    print(f"Preço total do pedido: R$ {preco}")
elif (codigo ==101):
    preco = quantidade *18
    print(f"Preço total do pedido: R$ {preco}")
elif (codigo ==102):
    preco = quantidade *20
    print(f"Preço total do pedido: R$ {preco}")
elif (codigo ==103):
    preco = quantidade *5
    print(f"Preço total do pedido: R$ {preco}")
elif (codigo ==104):
    preco = quantidade *15
    print(f"Preço total do pedido: R$ {preco}")
elif (codigo ==105):
    preco = quantidade *4
    print(f"Preço total do pedido: R$ {preco}")    
else:
    print("Erro: código do produto não reconhecido.")