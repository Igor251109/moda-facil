from registrar_venda import registrar_venda
from vereficar_produto import vereficar_produto
import consultar_produto import consultar_produto
from cadastros import cadastrar_cliente, cadastrar_funcionario, cadastrar_gerente
from cadastrar_produtos import cadastrar_produtos
from tratar_erros import tratar_erros_funcoes
from logins import login_funcionario, login_gerente

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

    except ValueError:
        print("Caracteres inválidos.")

def fazer_login():
    try:
        print("\n 1 - GERENTE | 2 - FUNCIONÁRIO | 3 - CLIENTE")
        opcao = int(input("Qual opção vai escolher?: "))

