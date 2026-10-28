from database import conectar

def listar_vendas():
    conexao = None

    try:
        conexao, cursor = conectar()

        cursor.execute('''SELECT * FROM vendas''')
        vendas = cursor.fetchall()

        if vendas:
            for venda in vendas:
                print(
                    f"| ID: {venda[0]} |"
                    f"| VALOR TOTAL: R${venda[1]:.2f} |"
                )
        
        else:
            print("Não há nenhuma venda realizada.")
    finally:
        if conexao:
            conexao.close()