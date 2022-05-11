from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contato_grupo = {
    '...':'Casa',
    '...':'Trabalho',
    'jrs':'Casa',
    'Maria':'Casa',
    'Jose':'Casa',
    'Roberth':'Trabalho',
    'Jeferson':'Trabalho',
    'Renato':'Trabalho',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Contatos associados!')