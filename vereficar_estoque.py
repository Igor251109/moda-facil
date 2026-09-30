from database import conectar

def consultar_produtos():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== CONSULTA DE PRODUTOS ====")

        cursor.execute("SELECT * FROM produtos ORDER BY produtos.tamanho")
        dados = cursor.fetchall()

        for produto in dados:
            print(f"Categoria: {produto[1]} | Preço: {produto[2]} |")
            print(f"Quantidade: {produto[3]} | Tamanho: {produto[4]}")
            print(f"Cor: {produto[5]} | Marca: {produto[6]} |")

            print("-" * 30)
    finally:
        if conexao:
            conexao.close()