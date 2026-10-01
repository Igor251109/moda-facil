from database import conectar


def verificar_produto():
    conexao = None

    try:
        conexao, cursor = conectar()

        qual_produto_buscar = {
            "categoria": input("Qual a categoria da peça de roupa?: ").lower(),
            "tamanho": input("Qual o tamanho da peça de roupa?: ").lower(),
            "marca": input("Qual a marca da peça de roupa?: ").lower(),
            "cor": input("Qual a cor da peça de roupa?: ").lower()
        }

        cursor.execute(
            '''SELECT categoria, tamanho, marca, cor, preco, quantidade
            FROM produtos
            WHERE categoria = ?
            AND tamanho = ?
            AND marca = ?
            AND cor = ?''',
            (
                qual_produto_buscar["categoria"],
                qual_produto_buscar["tamanho"],
                qual_produto_buscar["marca"],
                qual_produto_buscar["cor"]
            )
        )

        produto = cursor.fetchone()

        if produto:
            print("\nProduto encontrado!")
            print(f"Categoria: {produto[0]}")
            print(f"Tamanho: {produto[1]}")
            print(f"Marca: {produto[2]}")
            print(f"Cor: {produto[3]}")
            print(f"Preço: R${produto[4]:.2f}")
            print(f"Quantidade: {produto[5]}")
        else:
            print("Produto não encontrado.")

    finally:
        if conexao:
            conexao.close()