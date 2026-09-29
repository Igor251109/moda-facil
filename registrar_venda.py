from database import conectar

def registrar_venda():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE REALIZAÇÕES DE VENDAS ====")

        dados = {
            "categoria": input("qual a categoria do produto?: ")
            "tamanho": input("qual tamanho da peça de roupa que procura?: "),
            "marca": input("qual a marca desejada?: ")
        }

        cursor.execute("SELECT categoria, tamanho, marca, preco, id_produto FROM produtos WHERE categoria = ? AND tamanho = ? AND marca = ?",
        (dados["categoria"], dados["tamanho"], dados["marca"]))
        produtos = cursor.fetchall()

        if produtos:
            for produto in produtos:
                print(f"id: {produto[0]} | marca: {produto[6]} | categoria: {produto[1]} | tamanho: {produto[4]} | preço: {produto[2]}")
            
            idx = int(input("qual ID da peça que deseja comprar?: "))

            cursor.execute('''SELECT id_produto FROM produtos WHERE id_produto = ?''', (idx,))
            produto = cursor.fetchone()

            if produto:
                quantos_comprar = int(input("quantas peças deseja comprar?: "))

                cursor.execute('''SELECT quantidade FROM produtos WHERE quantidade = ?''', (idx,))
                quantidade = cursor.fetchone()

                if quantidade:
                    cursor.execute("DELETE quantidade FROM produtos WHERE id_produto = ?", (quantidade, idx))

                    print("venda realizada cum sucesso!")
                else:
                    print("quantidade indisponivel.")
                    return
            else:
                print("quantidade indisponivel.")
                return
        else:
            print("quantidade indisponivel.")
            return