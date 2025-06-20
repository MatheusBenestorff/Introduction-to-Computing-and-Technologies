import pandas as pd
from datetime import datetime

def atualiza_caixa(fruta, quantidade, usuario, codigoCaixa):
    dadosEstoque = pd.read_csv("Estoque.csv")
    dadosCaixa = pd.read_csv("Caixa.csv")

    lista_frutas = list(dadosEstoque['Fruta'])
    lista_quantidades = list(dadosEstoque['Quantidade'])
    lista_preco = list(dadosEstoque['PVenda'])
    lista_caixa = list(dadosCaixa['Caixa'])

    indice_fruta = lista_frutas.index(fruta)
    quantidade = lista_quantidades[indice_fruta]
    precoFruta = lista_preco[indice_fruta]
    caixa = lista_caixa[-1]

    if(codigoCaixa == 0):
        caixa = caixa + (quantidade * precoFruta)
    elif(codigoCaixa == 1):
        caixa = caixa - (quantidade * precoFruta)

    data_atual = datetime.now()

    dadosCaixa.loc[len(dadosCaixa)] = [caixa, usuario, data_atual]
    dadosCaixa.to_csv("Caixa.csv", index=False)

    return 0
