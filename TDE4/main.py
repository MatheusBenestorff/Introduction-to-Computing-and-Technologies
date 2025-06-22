import caixa
import estoque
import login
import sys
import os

def main():

    while True:
        print("<---------SISTEMA DE ESTOQUE--------->")
        print("1 = LOGIN")
        print("2 = CADASTRO DE USUÁRIO")
        print("3 = SAIR DO SISTEMA")
        print("--------------------------------------")
        print("")
        codigo_inicial = int(input("Digite o codigo da operação: "))

        if(codigo_inicial == 1):
            usuario = input("Digite o nome de Usuario: ")
            codigo_login = login.login(usuario)

            if(codigo_login == 1):
                print("")
                print("Este Usuario não existe.\n")
                continue
            elif(codigo_login == 2):
                print("")
                print("Senha incorreta.\n")
                continue
            else:
                os.system('cls')
                print(f"Bem vindo {usuario}!")

                while True:
                    print("")
                    print("<------------ESTOQUE ATUAL----------->")
                    print("")
                    estoque.mostrar_estoque()
                    print("")
                    print("--------------OPERAÇÕES---------------")
                    print("(1) Venda de Fruta")
                    print("(2) Compra de Fruta")
                    print("(3) Cadastro de nova Fruta")
                    print("(4) Gerar Gráfico dos itens em estoque")
                    print("(5) Voltar ao menu principal")
                    print("--------------------------------------\n")

                    codigo_operacao = int(input("Digite o código de operação: "))

                    if(codigo_operacao == 1):
                        while True:
                            fruta = input("Digite a fruta que deseja vender: ")    
                            quantidade = int(input("Digite a quantidade que deseja vender: "))
                            codigo_venda = estoque.venda_fruta(fruta, quantidade)

                            if(codigo_venda == 1):
                                os.system('cls')
                                print("Essa fruta não existe no estoque.")
                                break
                            elif(codigo_venda == 2):
                                os.system('cls')
                                print("Quantidade digitada é inválida.")
                                break
                            elif(codigo_venda == 3):
                                os.system('cls')
                                print("Quantidade insuficiente em estoque.")
                                break
                            else:
                                os.system('cls')
                                print("Venda realizada com sucesso.")
                                codigo_caixa = 1
                                caixa.atualiza_caixa(fruta, quantidade, usuario, codigo_caixa) 
                                print("Caixa atualizado.\n")
                                break

                    elif(codigo_operacao == 2):
                        while True:
                            fruta = input("Digite a fruta que deseja comprar: ")    
                            quantidade = int(input("Digite a quantidade que deseja comprar: "))
                            codigo_compra = estoque.compra_fruta(fruta, quantidade)

                            if(codigo_compra == 1):
                                os.system('cls')
                                print("Essa fruta não existe no estoque.")
                                break
                            elif(codigo_compra == 2):
                                os.system('cls')
                                print("Quantidade digitada é inválida.")
                                break
                            else:
                                os.system('cls')
                                print("Compra realizada com sucesso.")
                                codigo_caixa = 2
                                caixa.atualiza_caixa(fruta, quantidade, usuario, codigo_caixa) 
                                print("Caixa atualizado.\n")
                                break

                    elif(codigo_operacao == 3):
                        while True:
                            fruta = input("Digite a fruta que deseja cadastrar: ")    
                            codigo_cadastro = estoque.cadastra_fruta(fruta)

                            if(codigo_cadastro == 1):
                                os.system('cls')
                                print("Essa fruta já esta cadastrada no estoque.")
                                break    
                            elif(codigo_cadastro == 2):
                                os.system('cls')
                                print("Quantidade digitada é inválida.")
                                break   
                            else:
                                os.system('cls')
                                print(f"Fruta {fruta} cadastrada com sucesso.")
                                break

                    elif(codigo_operacao == 4):
                        while True:
                            estoque.gera_grafico()
                            os.system('cls')
                            break
                    elif(codigo_operacao == 5):
                        os.system('cls')
                        print("Voltando ao menu.\n")
                        break
                    else:
                        print("Código de operação inválido.")
                        break
                    
        elif(codigo_inicial == 2):
            usuario = input("Digite o nome de Usuario: ")
            codigo_cadastro = login.cadastro_usuario(usuario)

            if(codigo_cadastro == 1):
                print("Este Usuario já existe.\n")
                continue
            else:
                print(f"Usuário criado com sucesso! Faça login.\n")
                continue 
        elif(codigo_inicial == 3):
            os.system('cls')
            print("Saindo do sistema.\n")
            sys.exit()
        else:
            print("Codigo inválido! Tente novamente.\n")
            continue

main()