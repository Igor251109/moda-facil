from tratar_erros import tratar_erros_funcoes
from logins import login_funcionario, login_gerente

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