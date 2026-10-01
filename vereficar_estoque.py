from database import conectar


def consultar_produtos():
    conexao = None

    try:
        conexao, cursor = conectar()

        print("\n ==== CONSULTA DE PRODUTOS ====")

        cursor.execute("SELECT * FROM produtos ORDER BY tamanho")

        dados = cursor.fetchall()

        if not dados:
            print("Nenhum produto cadastrado.")
            return

        for produto in dados:
            print(f"ID: {produto[0]}")
            print(f"Categoria: {produto[1]} | Preço: R${produto[2]:.2f}")
            print(f"Quantidade: {produto[3]} | Tamanho: {produto[4]}")
            print(f"Cor: {produto[5]} | Marca: {produto[6]}")
            print("-" * 40)

    finally:
        if conexao:
            conexao.close()