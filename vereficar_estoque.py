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
            print(f"quantidade: {produto[3]} | tamanho: {produto[4]}")
            print(f"cor: {produto[5]} | marca: {produto[6]} |")

            print("-" * 30)
    finally:
        if conexao:
            conexao.close()