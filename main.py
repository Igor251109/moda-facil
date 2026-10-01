from registrar_venda import registrar_venda
from consultar_produto import verificar_produto
from vereficar_estoque import consultar_produtos
from cadastros import cadastrar_cliente, cadastrar_funcionario, cadastrar_gerente
from cadastrar_produtos import cadastrar_produtos
from tratar_erros import tratar_erros_funcoes
from logins import login_funcionario, login_gerente
from database import criar_tabela_clientes, criar_tabela_funcionarios, criar_tabela_gerente, criar_tabela_produtos

def criar_contas():
    try:
        print("\n 1 - GERENTE | 2 - FUNCIONÁRIO | 3 - CLIENTE")
        opcao = int(input("Qual opção vai escolher?: "))

        if opcao == 1:
            tratar_erros_funcoes(cadastrar_gerente)
        elif opcao == 2:
            tratar_erros_funcoes(cadastrar_funcionario)
        elif opcao == 3:
           tratar_erros_funcoes(cadastrar_cliente)
        else:
            print("Opção inválida.")
            return

    except ValueError:
        print("Caracteres inválidos.")

def fazer_login():
    print("\n1 - GERENTE | 2 - FUNCIONÁRIO")

    opcao = int(input("Qual opção vai escolher?: "))

    if opcao == 1:
        return tratar_erros_funcoes(login_gerente)

    elif opcao == 2:
        return tratar_erros_funcoes(login_funcionario)

    else:
        print("Opção inválida.")
        return False

def menu():
    while True:
        try:
            print("\n ==== MENU DO  USUÁRIO ====")
            oque_fazer = input("tem login?: ").lower()

            if oque_fazer in ["sim", "s"]:
                login = fazer_login()

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

            
            elif oque_fazer in ["nao", "n", "não"]:
                criar_contas()
            
            else:
                print("informações inválidas.")
                continue
        except ValueError:
            print("dados inválidos.")

criar_tabela_clientes()
criar_tabela_funcionarios()
criar_tabela_gerente()
criar_tabela_produtos()
tratar_erros_funcoes(menu)