import pandas as pd
from datetime import datetime

def aumenta_caixa(fruta, quantidade, usuario):
    dadosEstoque = pd.read_csv("Estoque.csv")
    dadosCaixa = pd.read_csv("Caixa.csv")

    lista_frutas = list(dadosEstoque['Fruta'])
    lista_preco = list(dadosEstoque['PVenda'])
    lista_caixa = list(dadosCaixa['Caixa'])

    indice_fruta = lista_frutas.index(fruta)
    precoFruta = lista_preco[indice_fruta]
    caixa = lista_caixa[-1]

    caixaAtual = caixa + (quantidade * precoFruta)

    data_atual = datetime.now()

    dadosCaixa.loc[len(dadosCaixa)] = [caixaAtual, usuario, data_atual]
    dadosCaixa.to_csv("Caixa.csv", index=False)

    return 0

def diminui_caixa(fruta, quantidade, usuario):
    dadosEstoque = pd.read_csv("Estoque.csv")
    dadosCaixa = pd.read_csv("Caixa.csv")

    lista_frutas = list(dadosEstoque['Fruta'])
    lista_preco = list(dadosEstoque['PCompra'])
    lista_caixa = list(dadosCaixa['Caixa'])

    indice_fruta = lista_frutas.index(fruta)
    precoFruta = lista_preco[indice_fruta]
    caixa = lista_caixa[-1]

    caixaAtual = caixa - (quantidade * precoFruta)

    data_atual = datetime.now()

    dadosCaixa.loc[len(dadosCaixa)] = [caixaAtual, usuario, data_atual]
    dadosCaixa.to_csv("Caixa.csv", index=False)

    return 0

