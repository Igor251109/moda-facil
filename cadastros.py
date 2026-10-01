from database import conectar


def cadastrar_funcionario():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n-----CADASTRAR FUNCIONÁRIO-----")

        nome_funcionario = input("Digite o seu nome: ").strip().lower()
        telefone_funcionario = input("Digite o seu telefone: ").strip()
        data_funcionario = input("Digite sua data de nascimento: ").strip()

        cursor.execute(
            """INSERT INTO funcionarios
            (nome_funcionario, telefone_funcionario, data_funcionario)
            VALUES (?, ?, ?)""",
            (nome_funcionario, telefone_funcionario, data_funcionario)
        )

        conexao.commit()

        print("\nFUNCIONÁRIO CADASTRADO COM SUCESSO!")

    finally:
        if conexao:
            conexao.close()


def cadastrar_gerente():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n-----CADASTRAR GERENTE-----")

        nome_gerente = input("Digite o seu nome: ").strip().lower()
        telefone_gerente = input("Digite o seu telefone: ").strip()
        data_gerente = input("Digite sua data de nascimento: ").strip()

        cursor.execute(
            """INSERT INTO gerentes
            (nome_gerente, telefone_gerente, data_nascimento)
            VALUES (?, ?, ?)""",
            (nome_gerente, telefone_gerente, data_gerente)
        )

        conexao.commit()

        print("\nGERENTE CADASTRADO COM SUCESSO!")

    finally:
        if conexao:
            conexao.close()


def cadastrar_cliente():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n-----CADASTRAR CLIENTE-----")

        nome_cliente = input("Digite o seu nome: ").lower()
        telefone_cliente = input("Digite o seu telefone: ")
        data_cliente = input("Digite sua data de nascimento: ")

        cursor.execute(
            '''INSERT INTO clientes
            (nome_cliente, telefone_cliente, data_cliente)
            VALUES (?, ?, ?)''',
            (nome_cliente, telefone_cliente, data_cliente)
        )

        conexao.commit()

        print("\nCLIENTE CADASTRADO COM SUCESSO!")

    finally:
        if conexao:
            conexao.close()