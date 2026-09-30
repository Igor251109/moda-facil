from database import conectar

def login_gerente():
    conexao = None
    try:
        conwxao, cursor = conectar()
        print('\n ==== SISTEMA DE LOGIN DE GERENTES ====')

        nome_gerente = input("Digite o seu nome: ").lower()
        telefone_gerente = input("Digite o seu telefone: ").lower()
        data_gerente = input("Digite sua data de nascimento: ").lower()

        cursor.execute('''SELECT nome_gerente, telefone_gerente, data_nascimento FROM gerentes WHERE nome_gerente = ? AND telefone_gerente = ? AND data_nascimento = ?''',
        (nome_gerente, telefone_gerente, data_gerente))
        gerente = cursor.fetchone()

        if gerente:
            return True
        else:
            return False


def login_funcionario():
    conexao = None
    try:
        conwxao, cursor = conectar()
        print('\n ==== SISTEMA DE LOGIN DE GERENTES ====')

        nome_funcionario = input("Digite o seu nome: ").lower()
        telefone_funcionario = input("Digite o seu telefone: ").lower()
        data_funcionario = input("Digite sua data de nascimento: ").lower()

        cursor.execute('''SELECT nome_funcionario, telefone_funcionario, data_funcionario FROM gerentes WHERE nome_funcionario = ? AND telefone_funcionario = ? AND data_funcionario = ?''',
        (nome_funcionario, telefone_funcionario, data_funcionario))
        funcionario = cursor.fetchone()

        if funcionario:
            return True
        else:
            return False