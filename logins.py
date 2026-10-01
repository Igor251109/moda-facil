from database import conectar


def login_gerente():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE LOGIN DE GERENTE ====")

        nome_gerente = input("Digite o seu nome: ").strip().lower()
        telefone_gerente = input("Digite o seu telefone: ").strip()
        data_gerente = input("Digite sua data de nascimento: ").strip()

        cursor.execute(
            """SELECT * FROM gerentes
            WHERE nome_gerente = ?
            AND telefone_gerente = ?
            AND data_nascimento = ?""",
            (nome_gerente, telefone_gerente, data_gerente)
        )

        gerente = cursor.fetchone()

        if gerente:
            print("\nLOGIN REALIZADO COM SUCESSO!")
            return True

        print("\nConta não encontrada.")
        return False

    finally:
        if conexao:
            conexao.close()


def login_funcionario():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE LOGIN DE FUNCIONÁRIO ====")

        nome_funcionario = input("Digite o seu nome: ").strip().lower()
        telefone_funcionario = input("Digite o seu telefone: ").strip()
        data_funcionario = input("Digite sua data de nascimento: ").strip()

        cursor.execute(
            """SELECT * FROM funcionarios
            WHERE nome_funcionario = ?
            AND telefone_funcionario = ?
            AND data_funcionario = ?""",
            (nome_funcionario, telefone_funcionario, data_funcionario)
        )

        funcionario = cursor.fetchone()

        if funcionario:
            print("\nLOGIN REALIZADO COM SUCESSO!")
            return True

        print("\nConta não encontrada.")
        return False

    finally:
        if conexao:
            conexao.close()