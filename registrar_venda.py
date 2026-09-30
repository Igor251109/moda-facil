from database import conectar

def registrar_venda():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE REALIZAÇÕES DE VENDAS ====")

        dados = {
            "categoria": input("Qual a categoria do produto?: ").lower(),
            "tamanho": input("Qual tamanho da peça de roupa que procura?: ").lower(),
            "marca": input("Qual a marca desejada?: ").lower()
        }

        cursor.execute("SELECT categoria, tamanho, marca, preco, id_produto FROM produtos WHERE categoria = ? AND tamanho = ? AND marca = ?",
        (dados["categoria"], dados["tamanho"], dados["marca"]))
        produtos = cursor.fetchall()

        if produtos:
            for produto in produtos:
                print(f"ID: {produto[0]} | Marca: {produto[6]} | Categoria: {produto[1]} | Tamanho: {produto[4]} | Preço: {produto[2]}")
            
            idx = int(input("Qual ID da peça que deseja comprar?: "))

            cursor.execute('''SELECT id_produto FROM produtos WHERE id_produto = ?''', (idx,))
            produto = cursor.fetchone()

            if produto:
                quantos_comprar = int(input("Quantas peças deseja comprar?: "))

                cursor.execute('''SELECT quantidade FROM produtos WHERE quantidade = ?''', (idx,))
                quantidade = cursor.fetchone()

                if quantidade:
                    cursor.execute("DELETE quantidade FROM produtos WHERE id_produto = ?", (quantidade, idx))

                    print("Venda realizada cum sucesso!")
                else:
                    print("Quantidade indisponivel.")
                    return
            else:
                print("Quantidade indisponivel.")
                return
        else:
            print("Quantidade indisponivel.")
            return
    finally:
        if conexao:
            conexao.close()
