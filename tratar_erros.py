import sqlite3


def tratar_erros_funcoes(funcao):
    try:
        return funcao()

    except KeyboardInterrupt:
        print("\nEncerrando sistema...")
        return False

    except ValueError:
        print("Dados inválidos.")
        return False

    except sqlite3.OperationalError as e:
        print("Erro operacional no banco de dados:", e)
        return False

    except sqlite3.IntegrityError as e:
        print("Erro de integridade no banco de dados:", e)
        return False

    except sqlite3.Error as e:
        print("Erro no banco de dados:", e)
        return False

    except Exception as e:
        print("Exceção:", e)
        return False