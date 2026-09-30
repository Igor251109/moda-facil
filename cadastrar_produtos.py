from database import conectar

def cadastrar_produtos():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE CADASTRAMENTO DE PRODUTOS ====")

        dados = {
            "categoria_produto": input("qual a categoria do produto?: ").lower(),
            "preco": float(input("qual o valor do produto?: ")).lower(),
            "quantidade": int(input("qual a quantidade que deseja adicionar a esse produto?: ")).lower(),
            "tamanho": input("qual o tamanho da peça (p, m, g, gg, xg)?: ").lower(),
            "cor": input("digite a cor da peça de roupa: ").lower(),
            "marca": input("qual a marca da peça de roupa?: ").lower()
        }

        cursor.execute('''INSERT INTO produtos (categoria, preco, quantidade, tamanho, cor, marca) VALUES (?, ?, ?, ?, ?, ?)''',
         (dados["categoria_produto"], dados["preco"], dados["quantidade"], dados["tamanho"], dados["cor"], dados["marca"]))

         print("produto(s) adicionadas com sucesso!")

         conexao.commit()
    finally:
        if conexao:
            conexao.close()