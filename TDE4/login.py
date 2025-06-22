import pandas as pd

#Função de cadastro de usuário
def cadastro_usuario(usuario):
    dados = pd.read_csv("Usuarios.csv")
    lista_usuarios = list(dados["Usuario"])

    #Usuário já existe
    if usuario in lista_usuarios:
        return 1

    senha = int(input("Escolha uma senha: "))
    senhaVerificada = int(input("Confirme sua senha: "))

    while (senhaVerificada != senha):
        senhaVerificada = int(input("As senhas não coincidem. Digite novamente sua senha: "))

    dados.loc[len(dados)] = [usuario, senha]
    dados.to_csv("Usuarios.csv", index=False)

    return 0

#Função para login de usuário
def login(usuario):
    dados = pd.read_csv("Usuarios.csv")
    lista_usuarios = list(dados["Usuario"])
    lista_senhas = list(dados["Senha"])

    #Usuário não existe
    if (usuario not in lista_usuarios):
        return 1
    
    senha = input("Digite a sua senha: ")

    indiceUsuario = lista_usuarios.index(usuario)
    senhaCorreta = str(lista_senhas[indiceUsuario])

    #Senhas incorreta
    if senha != senhaCorreta:
        return 2

    return 0


