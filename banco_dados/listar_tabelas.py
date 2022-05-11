from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('SHOW TABLES')
        
        for i, tabela in enumerate(cursor):
            print(tabela[i])
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')