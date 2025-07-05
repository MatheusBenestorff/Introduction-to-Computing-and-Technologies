import sys
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt

def cadastro_item(item):
    dados = pd.read_csv("Estoque.csv")
    lista_itens = list(dados['Item'])

    # Item já existe
    if (item in lista_itens):
        return 1

    quantidade = 0
    data_cadastro = formata_data()

    dados.loc[len(dados)] = [item, quantidade, data_cadastro ]
    dados.to_csv("Estoque.csv", index=False)

    return 0

def remover_item(item):
    dados = pd.read_csv("Estoque.csv")
    lista_itens = list(dados['Item'])

    # Item não existe
    if (item not in lista_itens):
        return 1

    indice_item = lista_itens.index(item)
    dados = dados.drop(indice_item)
    dados.to_csv("Estoque.csv", index=False)

    return 0

def adicionar_quantidade(item):
    dados = pd.read_csv("Estoque.csv")
    lista_itens = list(dados["Item"])
    lista_quantidades = list(dados["Quantidade"])
    lista_datas_cadastro = list(dados["DataCadastro"])

    # Item não existe na tabela
    if (item not in lista_itens):
        return 1

    quantidade = int(input("Digite a quantidade a ser adicionada: "))

    # Quantidade inválida
    if (quantidade <= 0):
        return 2

    indice_item = lista_itens.index(item)
    qtd_existente = lista_quantidades[indice_item]
    qtd_existente = qtd_existente + quantidade
    data_cadastro = lista_datas_cadastro[indice_item]

    dados.loc[indice_item] = [item, qtd_existente, data_cadastro]
    dados.to_csv("Estoque.csv", index=False)

    return 0

def remover_quantidade(item):
    dados = pd.read_csv("Estoque.csv")
    lista_itens = list(dados["Item"])
    lista_quantidades = list(dados["Quantidade"])
    lista_datas_cadastro = list(dados["DataCadastro"])

    # Item não existe na tabela
    if (item not in lista_itens):
        return 1

    quantidade = int(input("Digite a quantidade a ser removida: "))

    # Quantidade inválida
    if (quantidade <= 0):
        return 2

    indice_item = lista_itens.index(item)
    qtd_existente = lista_quantidades[indice_item]
    qtd_existente = qtd_existente - quantidade
    data_cadastro = lista_datas_cadastro[indice_item]

    #Quantidade insuficiente
    if(qtd_existente - quantidade < 0):
        return 3

    dados.loc[indice_item] = [item, qtd_existente, data_cadastro]
    dados.to_csv("Estoque.csv", index=False)

    return 0

def gerar_grafico():
    dados = pd.read_csv("Estoque.csv")

    lista_itens = list(dados["Item"])
    lista_quantidades = list(dados["Quantidade"])

    item = lista_itens
    quantidades = lista_quantidades

    total = sum(quantidades)

    plt.pie(quantidades, labels=item, autopct=lambda p: '{:.0f}'.format(p * total /100), shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()

def mostrar_estoque():
    dados = pd.read_csv("Estoque.csv")
    print(dados)

def formata_data():
    data = datetime.now()
    data_formatada = data.strftime("%Y-%m-%d %H:%M:%S")
    return data_formatada

def main():
    while True:
        print("<---------SISTEMA DE ESTOQUE FERRAGEM--------->")
        print("1 = CADASTRO DE NOVO ITEM")
        print("2 = REMOVER UM ITEM")
        print("3 = ADICIONAR QUANTIDADE")
        print("4 = REMOVER QUANTIDADE")
        print("5 = GERAR GRÁFICO DE PIZZA")
        print("6 = MOSTRAR ESTOQUE")
        print("7 = SAIR DO SISTEMA")
        print("----------------------------------------------")
        print("")

        codigo = 0
        while codigo != 1 and codigo !=2 and codigo !=3 and codigo !=4 and codigo !=5 and codigo !=6 and codigo !=7:
            codigo = int(input("Digite o codigo da operação: "))

        if (codigo == 1):
            while True:
                item = input("Digite o novo item que deseja cadastrar: ")
                codigo_cadastro = cadastro_item(item)

                if (codigo_cadastro == 1):
                    print("\nEsse item já esta cadastrado no estoque.\n")
                    break
                else:
                    print(f"\nItem {item} cadastrado com sucesso.\n")
                    break

        elif (codigo == 2):
            while True:
                item = input("Digite o item que deseja remover: ")
                codigo_remove_item = remover_item(item)

                if (codigo_remove_item == 1):
                    print("\nEsse item não existe no estoque.\n")
                    break
                else:
                    print(f"\nItem {item} foi removido com sucesso.\n")
                    break

        elif (codigo == 3):
            while True:
                item = input("Digite o item a ter a quantidade adicionada: ")
                codigo_adicionar_quantidade = adicionar_quantidade(item)

                if (codigo_adicionar_quantidade == 1):
                    print("\nEsse item não existe no estoque.\n")
                    break
                elif (codigo_adicionar_quantidade == 2):
                    print("\nQuantidade digitada é inválida.\n")
                    break
                else:
                    print("\nQuantidade adicionada com sucesso.\n")
                    break

        elif (codigo == 4):
            while True:
                item = input("Digite o item a ter a quantidade removida: ")
                codigo_remover_quantidade = remover_quantidade(item)

                if (codigo_remover_quantidade == 1):
                    print("\nEsse item não existe no estoque.\n")
                    break
                elif (codigo_remover_quantidade == 2):
                    print("\nQuantidade digitada é inválida.\n")
                    break
                elif (codigo_remover_quantidade == 3):
                    print("\nQuantidade insuficiente em estoque.\n")
                    break
                else:
                    print("\nQuantidade removida com sucesso.\n")
                    break

        elif (codigo == 5):
            while True:
                gerar_grafico()
                print("")
                break

        elif (codigo == 6):
            while True:
                print("<------------------ESTOQUE----------------->")
                mostrar_estoque()
                print("--------------------------------------------")
                print("")
                voltar = int(input("Digite 1 para voltar ao menu: "))
                while voltar != 1:
                    voltar = int(input("Digite 1 para voltar ao menu: "))
                if (voltar == 1):
                    print("")
                    break

        elif (codigo == 7):
            print("\nSaindo do sistema...")
            sys.exit()

main()