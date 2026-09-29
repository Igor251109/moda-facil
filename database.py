import sqlite3

def conectar():
    conexao = sqlite3.connect("moda_facil.db")
    cursor = conexao.cursor()

    return conexao, cursor

def criar_tabela_gerente():
    conexao = None 

    try:
        conexao, cursor = conectar()

        cursor.execute('''CREATE TABLE IF NOTE EXISTS gerentes (
            id_gerente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_gerente TEXT NOT NULL,
            telefone_gerente TEXT NOT NULL,
            data_nascimento TEXT NOT NULL
        )
        ''')

        conexao.commit()
    finally:
        if conexao:
            conexao.close()

def criar_tabela_funcionarios():
    conexao = None 

    try:
        conexao, cursor = conectar()

        cursor.execute('''CREATE TABLE IF NOTE EXISTS funcionarios (
            id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_funcionario TEXT NOT NULL,
            telefone_funcionario TEXT NOT NULL,
            data_funcionario TEXT NOT NULL
        )
        ''')

        conexao.commit()
    finally:
        if conexao:
            conexao.close()

def criar_tabela_produtos():
    conexao = None

    try:
        conexao, cursor = conectar()

        cursor.execute('''CREATE TABLE IF NOT EXISTS produtos(
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            tamanho TEXT NOT NULL,
            cor TEXT NOT NULL,
            marca TEXT NOT NULL
        )
        ''')

        conexao.commit()

    finally:
        if conexao:
            conexao.close()
