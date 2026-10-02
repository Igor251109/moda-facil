from cadastros import cadastrar_funcionario, cadastrar_gerente
from tratar_erros import tratar_erros_funcoes

def criar_contas_gerente():
    print("\n ==== CRIAR CONTA PARA GERENTES ==== ")
        
    tratar_erros_funcoes(cadastrar_gerente)
        

def criar_contas_funcionarios():
    print("\n ==== CRIAR CONTA FUNCIONÁRIOS ====")

    tratar_erros_funcoes(cadastrar_funcionario)