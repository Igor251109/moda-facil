from database import conectar

def cadastrar_produtos():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE CADASTRAMENTO DE PRODUTOS ====")

        dados = {
            "categoria_produto": input("qual a categoria do produto?: "),
            "preco": float(input("qual o valor do produto?: ")),
            "quantidade": int(input("qual a quantidade que deseja adicionar a esse produto?: ")),
            "tamanho": input("qual o tamanho da peça (p, m, g, gg, xg)?: "),
            "cor": input("digite a cor da peça de roupa: "),
            "marca": input("qual a marca da peça de roupa?: ")
        }

        cursor.execute('''INSERT INTO produtos (categoria, preco, quantidade, tamanho, cor, marca) VALUES (?, ?, ?, ?, ?, ?)''',
         (dados["categoria_produto"], dados["preco"], dados["quantidade"], dados["tamanho"], dados["cor"], dados["marca"]))

         print("produto(s) adicionadas com sucesso!")

         conexao.commit()
    finally:
        if conexao:
            conexao.close()