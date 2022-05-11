from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
)

cursor = conexao.cursor()
# CREATE IF NOT EXISTS agenda
cursor.execute('CREATE DATABASE agenda')