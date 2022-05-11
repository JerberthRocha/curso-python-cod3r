from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = "UPDATE contatos SET nome = 'jrs' WHERE id = 4"

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) atualizado(s).')