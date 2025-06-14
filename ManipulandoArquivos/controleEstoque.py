import pandas as pd

def vende_fruta(fruta, quantidade, arquivo):
    dados = pd.read_csv(arquivo)

    lista_frutas = list(dados['Fruta'])
    lista_quantidades = list(dados['Quantidade'])

    if (fruta not in lista_frutas):  # A fruta NÃO existe no estoque
        return 1
    indice_fruta = lista_frutas.index(fruta)
    qtd_existente = lista_quantidades[indice_fruta]

    if (quantidade <= 0):
        return 3

    if(qtd_existente - quantidade < 0):
        return 2

    dados.loc[indice_fruta] = [fruta, qtd_existente - quantidade]
    dados.to_csv(arquivo, index=False)
    return 0

def compra_fruta(fruta, quantidade, arquivo):
    dados = pd.read_csv(arquivo)

    lista_frutas = list(dados["Fruta"])
    lista_quantidades = list(dados["Quantidade"])

    if (fruta not in lista_frutas):
        dados.loc[len(dados)] = [fruta, quantidade]
    else:
        indice_fruta = lista_frutas.index(fruta)
        qtd_existente = lista_quantidades[indice_fruta]
        dados.loc[indice_fruta] = [fruta, qtd_existente + quantidade]

    dados.to_csv(arquivo, index=False)
    return 0

print("(1) Venda")
print("(2) Compra")
codigo_operacao = int(input("Digite o código de operação: "))

if codigo_operacao == 1:

    fruta_vendida = input("Digite a fruta a ser vendida: ")
    qtd_vendida = int(input("Digite a quantidade a ser vendida: "))
    codigo_erro = vende_fruta(fruta_vendida, qtd_vendida, "Estoque.csv")

    if (codigo_erro == 0):
        print("Venda efetuda com sucesso!")
    else:
        print("Bro you're alone in this 🙏")


elif codigo_operacao == 2:
    fruta_comprada = input("Digite a fruta a ser comprada: ")
    qtd_comprada = int(input("Digite a quantidade a ser comprada: "))
    codigo_erro = compra_fruta(fruta_comprada, qtd_comprada, "Estoque.csv")

    if (codigo_erro == 0):
        print("Compra efetuda com sucesso!")
    else:
        print("Bro you're alone in this 🙏")














