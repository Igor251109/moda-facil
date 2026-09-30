import sqlite3

def tratar_erros_funcoes(funcao):
    try:
        funcao()
    except keyboardinterrupt:
        print("encerrando sistema...")
        return
    except ValueError:
        print("dados inválidos.")
        return
    except sqlite3.OperationalError as e:
        print("erro operacional no banco de dados:", e)
        return
    except sqlite3.IntregityError as e:
        print("erro de intregidade no banco de dados.", e)
        return
    except sqlite3.Error as e:
        print("erro no banco de dados:", e)
        return
    except Exception as e:
        print("exceção:", e)