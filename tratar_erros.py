import sqlite3

def tratar_erros_funcoes(funcao):
    try:
        funcao()
    except keyboardinterrupt:
        print("Encerrando sistema...")
        return
    except ValueError:
        print("Dados inválidos.")
        return
    except sqlite3.OperationalError as e:
        print("Erro operacional no banco de dados:", e)
        return
    except sqlite3.IntregityError as e:
        print("Erro de intregidade no banco de dados.", e)
        return
    except sqlite3.Error as e:
        print("Erro no banco de dados:", e)
        return
    except Exception as e:
        print("Exceção:", e)