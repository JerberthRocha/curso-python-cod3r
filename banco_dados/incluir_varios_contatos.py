from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO contatos (nome, telefone) VALUES (%s, %s)'
args = (
    ('Jerberth', '12340-3204'),
    ('Maria', '12349-3354'),
    ('Jose', '12348-3944'),
    ('Roberth', '12346-3334'),
    ('Jeferson', '12344-3234'),
    ('Renato', '22444-3234'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) incluído(s)!')