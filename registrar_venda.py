from database import conectar


def registrar_venda():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE REALIZAÇÃO DE VENDAS ====")

        dados = {
            "categoria": input("Qual a categoria do produto?: ").lower(),
            "tamanho": input("Qual tamanho da peça de roupa que procura?: ").lower(),
            "marca": input("Qual a marca desejada?: ").lower()
        }

        cursor.execute(
            '''SELECT id_produto, categoria, tamanho, marca, preco, cor, quantidade
            FROM produtos
            WHERE categoria = ?
            AND tamanho = ?
            AND marca = ?''',
            (
                dados["categoria"],
                dados["tamanho"],
                dados["marca"]
            )
        )

        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto encontrado.")
            return

        print("\nProdutos encontrados:")

        for produto in produtos:
            print(
                f"ID: {produto[0]} | "
                f"Categoria: {produto[1]} | "
                f"Tamanho: {produto[2]} | "
                f"Marca: {produto[3]} | "
                f"Preço: R${produto[4]:.2f} | "
                f"Cor: {produto[5]} | "
                f"Estoque: {produto[6]}"
            )

        idx = int(input("\nQual ID da peça que deseja comprar?: "))

        cursor.execute(
            '''SELECT quantidade, preco
            FROM produtos
            WHERE id_produto = ?''',
            (idx,)
        )

        produto = cursor.fetchone()

        if not produto:
            print("Produto não encontrado.")
            return

        quantidade_disponivel = produto[0]
        preco = produto[1]

        quantos_comprar = int(input("Quantas peças deseja comprar?: "))

        if quantos_comprar <= 0:
            print("Quantidade inválida.")
            return

        if quantos_comprar > quantidade_disponivel:
            print("Quantidade indisponível.")
            print(f"Estoque atual: {quantidade_disponivel}")
            return

        nova_quantidade = quantidade_disponivel - quantos_comprar

        cursor.execute(
            '''UPDATE produtos
            SET quantidade = ?
            WHERE id_produto = ?''',
            (nova_quantidade, idx)
        )

        conexao.commit()

        valor_total = preco * quantos_comprar

        print("\nVenda realizada com sucesso!")
        print(f"Quantidade vendida: {quantos_comprar}")
        print(f"Valor total: R${valor_total:.2f}")
        print(f"Estoque restante: {nova_quantidade}")

    finally:
        if conexao:
            conexao.close()
