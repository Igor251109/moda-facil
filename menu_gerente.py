from registrar_venda import registrar_venda
from consultar_produto import verificar_produto
from vereficar_estoque import consultar_produtos
from cadastros import cadastrar_cliente
from cadastrar_produtos import cadastrar_produtos
from tratar_erros import tratar_erros_funcoes
from criar_contas import criar_contas_gerente
from logins import login_gerente


def menu_gerente():
    while True:
        try:
            print("\n ==== MENU DO GERENTE ====")
            oque_fazer = input("tem login?: ").lower()

            if oque_fazer in ["sim", "s", "SIM"]:
                login = login_gerente()

                if login == True:

                    while True:
                        print("\n ==== MENU DO SISTEMA ====")
                        print("1 - CADASTRAR PRODUTOS")
                        print("2 - CONSULTAR PRODUTO")
                        print("3 - CADASTRAR CLIENTE")
                        print("4 - VERIFICAR ESTOQUE")
                        print("5 - REGISTRAR VENDA")
                        print("6 - SAIR")

                        qual_escolher = int(input("Qual opção vai escolher?: "))

                        match qual_escolher:
                            case 1:
                                tratar_erros_funcoes(cadastrar_produtos)
                            case 2:
                                tratar_erros_funcoes(verificar_produto)
                            case 3:
                                tratar_erros_funcoes(cadastrar_cliente)
                            case 4:
                                tratar_erros_funcoes(consultar_produtos)
                            case 5:
                                tratar_erros_funcoes(registrar_venda)
                            case 6:
                                print("Saindo da conta...")
                                break
                            case _:
                                print("Opção inválida.")

            
            elif oque_fazer in ["nao", "n", "não", "NAO", "NÃO"]:
                criar_contas_gerente()
            
            else:
                print("informações inválidas.")
                continue
        except ValueError:
            print("dados inválidos.")