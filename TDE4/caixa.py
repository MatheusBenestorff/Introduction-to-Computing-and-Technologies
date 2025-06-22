import pandas as pd
from datetime import datetime


#Função para atualizar o caixa
def atualiza_caixa(fruta, quantidade, usuario, codigo_caixa):
    dadosEstoque = pd.read_csv("Estoque.csv")
    dadosCaixa = pd.read_csv("Caixa.csv")

    lista_frutas = list(dadosEstoque['Fruta'])
    lista_pCompra = list(dadosEstoque['PCompra'])
    lista_pVenda = list(dadosEstoque['PVenda'])
    lista_caixa = list(dadosCaixa['Caixa'])

    indice_fruta = lista_frutas.index(fruta)
    preco_venda = lista_pVenda[indice_fruta]
    preco_compra = lista_pCompra[indice_fruta]

    #Último valor em caixa da tabela
    caixa = lista_caixa[-1]

    #O codigo é passado por parâmetro dependendo da operação realizada pelo usuário
    if(codigo_caixa == 1):
        #Venda de fruta
        caixa_atual = caixa + (quantidade * preco_venda)
    elif(codigo_caixa == 2):
        #Compra de fruta
        caixa_atual = caixa - (quantidade * preco_compra)

    data_atual = formata_data()

    dadosCaixa.loc[len(dadosCaixa)] = [caixa_atual, usuario, data_atual]
    dadosCaixa.to_csv("Caixa.csv", index=False)

    return 0

#Função auxiliar para formatar datetime.now()
def formata_data():
    data = datetime.now()
    data_formatada = data.strftime("%d/%m/%Y")
    return data_formatada

def mostrar_historico():
    dadosCaixa = pd.read_csv("Caixa.csv")
    print(dadosCaixa)




