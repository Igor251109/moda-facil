from registrar_venda import registrar_venda
from consultar_produto import verificar_produto
from vereficar_estoque import consultar_produtos
from cadastros import cadastrar_cliente
from tratar_erros import tratar_erros_funcoes
from fazer_logins import fazer_login
from criar_contas import criar_contas_funcionarios



def menu_funcionario():
    while True:
        try:
            print("\n ==== MENU DO FUNCIONÁRIO ====")
            oque_fazer = input("tem login?: ").lower()

            if oque_fazer in ["sim", "s", "SIM"]:
                login = fazer_login()

                if login == True:

                    while True:
                        print("\n ==== MENU DO FUNCIONÁRIO ====")
                        print("1 - CONSULTAR PRODUTOS")
                        print("2 - CADASTRAR CLIENTE")
                        print("3 - VERIFICAR ESTOQUE")
                        print("4 - REGISTRAR VENDA")
                        print("5 - SAIR")

                        qual_escolher = int(input("Qual opção vai escolher?: "))

                        match qual_escolher:
                            case 1:
                                tratar_erros_funcoes(consultar_produtos)
                            case 2:
                                tratar_erros_funcoes(cadastrar_cliente)
                            case 3:
                                tratar_erros_funcoes(verificar_produto)
                            case 4:
                                tratar_erros_funcoes(registrar_venda)
                            case 5:
                                print("encerrando programa...")
                                break
                            case _:
                                print("Opção inválida.")
                                break

            
            elif oque_fazer in ["nao", "n", "não", "NAO", "NÃO"]:
                criar_contas_funcionarios()
            
            else:
                print("informações inválidas.")
                continue
        except ValueError:
            print("dados inválidos.")