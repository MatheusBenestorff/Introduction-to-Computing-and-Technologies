import caixa
import estoque
import login
import sys

def main():

    while True:
        print("SISTEMA DE ESTOQUE")
        print("---------------------------")
        print("1 = LOGIN")
        print("2 = CADASTRO DE USUÁRIO")
        print("3 = SAIR DO SISTEMA")
        
        codigo_inicial = int(input("Digite o codigo da operação: "))

        if(codigo_inicial == 1):
            usuario = input("Digite o nome de Usuario: ")
            codigo_login = login.login(usuario)

            if(codigo_login == 1):
                print("Este Usuario não existe.\n")
                continue
            elif(codigo_login == 2):
                print("Senha incorreta.\n")
                continue
            else:
                print(f"Bem vindo ao sistema {usuario}!")

                while True:
                    print("")
                    print("ESTOQUE ATUAL")
                    estoque.mostrar_estoque()
                    print("---------------------------")
                    print("(1) Venda de Fruta")
                    print("(2) Compra de Fruta")
                    print("(3) Cadastro de nova Fruta")
                    print("(4) Gerar Gráfico dos itens em estoque")

                    codigo_operacao = int(input("Digite o código de operação: "))

                    if(codigo_operacao == 1):
                        fruta = input("Digite a fruta que deseja vender: ")    
                        quantidade = input("Digite a quantidade que deseja vender: ")
                        codigo_venda = estoque.venda_fruta(fruta, quantidade)

                    elif(codigo_operacao == 2):
                        fruta = input("Digite a fruta que deseja comprar: ")    
                        quantidade = input("Digite a quantidade que deseja comprar: ")
                        codigo_compra = estoque.compra_fruta(fruta, quantidade)

                    elif(codigo_operacao == 3):
                        fruta = input("Digite a fruta que deseja cadastrar: ")    
                        quantidade = input("Digite a quantidade que deseja cadastrar: ")
                        codigo_cadastro = estoque.cadastra_fruta(fruta, quantidade)

                    elif(codigo_operacao == 4):
                        pass
                    else:
                        pass
        elif(codigo_inicial == 2):
            pass
        elif(codigo_inicial == 3):
            print("Saindo do sistema.\n")
            sys.exit()
        else:
            print("Codigo inválido! Tente novamente.\n")
            continue

main()