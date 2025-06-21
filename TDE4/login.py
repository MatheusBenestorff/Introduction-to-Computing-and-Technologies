import pandas as pd

def cadastro_usuario(usuario):
    dados = pd.read_csv("Usuarios.csv")
    lista_usuarios = list(dados["Usuario"])

    if usuario in lista_usuarios:
        return 1

    senha = int(input("Escolha uma senha: "))
    senhaVerificada = int(input("Confirme sua senha: "))

    while (senhaVerificada != senha):
        senhaVerificada = int(input("As senhas não coincidem. Digite novamente sua senha: "))

    dados.loc[len(dados)] = [usuario, senha]
    dados.to_csv("Usuarios.csv", index=False)

    return 0

def login(usuario):
    dados = pd.read_csv("Usuarios.csv")
    lista_usuarios = list(dados["Usuario"])
    lista_senhas = list(dados["Senha"])

    if (usuario not in lista_usuarios):
        return 1
    
    senha = input("Digite a sua senha: ")

    indiceUsuario = lista_usuarios.index(usuario)
    senhaCorreta = str(lista_senhas[indiceUsuario])

    if senha != senhaCorreta:
        return 2

    return 0


