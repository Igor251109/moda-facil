from database import conectar

def vereficar_produto():
    conexao = None

    try:
        conexao, cursor = conectar()

        qual_produto_buscar = {
            "categoria": input("qual a categoria da peça de roupa?: ").lower(),
            "tamanho": input("qual o tamanho da peça de roupa?: ").lower(),
            "marca": input("qual a marca da peça de roupa?: ").lower(),
            "cor": input("qual a cor da peça de roupa?: ").lower()
        }

        cursor.execute('''SELECT categoria, tamanho, marca, cor FROM produtos WHERE categoria = ? AND tamanho = ? AND marca = ? AND cor = ?''', 
        (qual_produto_buscar["categoria"], qual_produto_buscar["tamanho"], qual_produto_buscar["marca"], qual_produto_buscar["cor"]))
        produto = cursor.fetchone()

        if produto:
            print("produto achado!")
            print(produto)
        
        else:
            print("produto não encontrado...")
            return