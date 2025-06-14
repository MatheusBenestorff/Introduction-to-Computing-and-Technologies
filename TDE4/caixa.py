import pandas as pd

def aumenta_caixa(fruta, quantidade, usuario):
    dadosEstoque = pd.read_csv("Estoque.csv")
    dadosCaixa = pd.read_csv("Caixa.csv")

    lista_frutas = list(dadosEstoque['Fruta'])
    lista_quantidades = list(dadosEstoque['Quantidade'])
    lista_preco = list(dadosEstoque['PVenda'])





    dados = pd.read_csv("Estoque.csv")

    lista_frutas = list(dados['Fruta'])
    lista_quantidades = list(dados['Quantidade'])


    if (fruta not in lista_frutas):
        print("Essa fruta não existe no estoque.")
        return 1

    indice_fruta = lista_frutas.index(fruta)
    qtd_existente = lista_quantidades[indice_fruta]

    #Quantidade inválida
    if (quantidade <= 0):
        print("Quantidade digitada é inválida.")
        return 2

    if(qtd_existente - quantidade < 0):
        print("Não existe a quantidade suficiente em estoque.")
        return 3

    dados.loc[indice_fruta] = [fruta, qtd_existente - quantidade]
    dados.to_csv("Estoque.csv", index=False)

    return 0