import pandas as pd

dados = pd.read_csv("SistemaLogin.csv")
contas = list(dados["usuarios"].values)
senhas = list(dados["senhas"].values)

opcao = 0
while(opcao !=1 and opcao != 2):
    opcao = int(input("Digite 1 para entrar ou 2 para registrar uma nova conta: "))

if(opcao == 1): #Entrar em uma conta
    usuarioDigitado = ''
    while(usuarioDigitado not in contas):
        usuarioDigitado = str(input("Digite o nome de Usuário: "))

        if (usuarioDigitado not in contas):
            print("Este usuario não existe. Tente novamente.")

    indiceUsuario = contas.index(usuarioDigitado)
    senhaCorreta = senhas[indiceUsuario]

    senhaDigitada = ''

    while(senhaDigitada != senhaCorreta):
        senhaDigitada = int(input("Digite a sua senha: "))

    print("Login realizado!")


if(opcao == 2): #Registrar uma nova conta

    usuarioDigitado = str(input("Escolha um nome de usuário: "))
    while(usuarioDigitado in contas):
        usuarioDigitado = str(input("Escolha outro nome de usuário: "))

    senhaDigitada = int(input("Escolha uma senha: "))
    senhaVerificada = int(input("Confirme sua senha: "))

    while (senhaVerificada != senhaDigitada):
        senhaVerificada = int(input("As senhas não coincidem. Digite novamente sua senha: "))

    dados.loc[len(dados)] = [usuarioDigitado, senhaDigitada]
    dados.to_csv("SistemaLogin.csv", index=False)

    print("Cadastro realizado!")
