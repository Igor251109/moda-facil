from database import conectar


def cadastrar_produtos():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE CADASTRAMENTO DE PRODUTOS ====")

        dados = {
            "categoria_produto": input("Qual a categoria do produto?: ").lower(),
            "preco": float(input("Qual o valor do produto?: ")),
            "quantidade": int(input("Qual a quantidade que deseja adicionar a esse produto?: ")),
            "tamanho": input("Qual o tamanho da peça (p, m, g, gg, xg)?: ").lower(),
            "cor": input("Digite a cor da peça de roupa: ").lower(),
            "marca": input("Qual a marca da peça de roupa?: ").lower()
        }

        cursor.execute(
            '''INSERT INTO produtos 
            (categoria, preco, quantidade, tamanho, cor, marca)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (
                dados["categoria_produto"],
                dados["preco"],
                dados["quantidade"],
                dados["tamanho"],
                dados["cor"],
                dados["marca"]
            )
        )

        conexao.commit()

        print("Produto(s) adicionado(s) com sucesso!")

    finally:
        if conexao:
            conexao.close()