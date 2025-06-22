import pandas as pd
import matplotlib.pyplot as plt

#Função para exibir o estoque
def mostrar_estoque():
    dados = pd.read_csv("Estoque.csv")
    print(dados)

def venda_fruta(fruta, quantidade):
    dados = pd.read_csv("Estoque.csv")

    lista_frutas = list(dados['Fruta'])
    lista_quantidades = list(dados['Quantidade'])
    lista_pVenda = list(dados['PVenda'])
    lista_pCompra = list(dados['PCompra'])

    #Fruta não existe
    if (fruta not in lista_frutas):
        return 1

    indice_fruta = lista_frutas.index(fruta)
    qtd_existente = lista_quantidades[indice_fruta]
    pVenda = lista_pVenda[indice_fruta]
    pCompra = lista_pCompra[indice_fruta]

    #Quantidade inválida
    if (quantidade <= 0):
        return 2

    #Quantidade insuficiente
    if(qtd_existente - quantidade < 0):
        return 3

    qtd_existente = qtd_existente - quantidade
    dados.loc[indice_fruta] = [fruta, qtd_existente, pVenda, pCompra]
    dados.to_csv("Estoque.csv", index=False)

    return 0

def compra_fruta(fruta, quantidade):
    dados = pd.read_csv("Estoque.csv")

    lista_frutas = list(dados["Fruta"])
    lista_quantidades = list(dados["Quantidade"])
    lista_pVenda = list(dados['PVenda'])
    lista_pCompra = list(dados['PCompra'])

    #Fruta não existe na tabela
    if (fruta not in lista_frutas):
        return 1
    
    #Quantidade inválida
    if (quantidade <= 0):
        return 2

    indice_fruta = lista_frutas.index(fruta)
    qtd_existente = lista_quantidades[indice_fruta]
    pVenda = lista_pVenda[indice_fruta]
    pCompra = lista_pCompra[indice_fruta]

    qtd_existente = qtd_existente + quantidade
    dados.loc[indice_fruta] = [fruta, qtd_existente, pVenda, pCompra]
    dados.to_csv("Estoque.csv", index=False)

    return 0

def cadastra_fruta(fruta):
    dados = pd.read_csv("Estoque.csv")
    lista_frutas = list(dados['Fruta'])

    #Fruta já existe
    if (fruta in lista_frutas):
        return 1
    
    quantidade = int(input("Digite a quantidade: "))
    pVenda = input("Digite o preço de Venda: ")
    pCompra = input("Digite o preço de Compra: ")
    
    #Quantidade inválida
    if (quantidade < 0):
        return 2
    
    dados.loc[len(dados)] = [fruta, quantidade, pVenda, pCompra]
    dados.to_csv("Estoque.csv", index=False)

    return 0


def gera_grafico():

    dados = pd.read_csv("Estoque.csv")

    lista_frutas = list(dados["Fruta"])
    lista_quantidades = list(dados["Quantidade"])

    frutas = lista_frutas
    quantidades = lista_quantidades

    total = sum(quantidades)

    plt.pie(quantidades, labels=frutas, autopct=lambda p: '{:.0f}'.format(p * total /100), shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()
