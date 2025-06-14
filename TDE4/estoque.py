import pandas as pd

def venda_fruta(fruta, quantidade):
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

def compra_fruta(fruta, quantidade):
    dados = pd.read_csv("Estoque.csv")

    lista_frutas = list(dados["Fruta"])
    lista_quantidades = list(dados["Quantidade"])

    #Fruta não existe na tabela
    if (fruta not in lista_frutas):
        return 1

    indice_fruta = lista_frutas.index(fruta)
    qtd_existente = lista_quantidades[indice_fruta]
    dados.loc[indice_fruta] = [fruta, qtd_existente + quantidade]

    dados.to_csv("Estoque.csv", index=False)
    return 0