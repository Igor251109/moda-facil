from database import criar_tabela_clientes, criar_tabela_funcionarios, criar_tabela_gerente, criar_tabela_produtos
from menu_funcionario import menu_funcionario
from menu_gerente import menu_gerente
from tratar_erros import tratar_erros_funcoes

def menu():
    try:
        while True:
            print("\n ==== MENU DO USUÁRIO ====")
            print("| 1 - GERENTE | 2 - FUNCIONÁRIO |")
            opcao = int(input("Qual opção vai escolher?: "))

            if opcao == 1:
                tratar_erros_funcoes(menu_gerente)
            
            elif opcao == 2:
                tratar_erros_funcoes(menu_funcionario)
            
            else:
                print("opção inválida.")
                continue
    except ValueError:
        print("Dados inválidos. Tente novamente.")


criar_tabela_clientes()
criar_tabela_funcionarios()
criar_tabela_gerente()
criar_tabela_produtos()
tratar_erros_funcoes(menu)