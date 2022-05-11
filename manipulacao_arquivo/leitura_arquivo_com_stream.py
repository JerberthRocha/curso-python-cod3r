# NÃO CARREGA TODOS OS DADOS NA MEMÓRIA, SOMENTE QUANDO NECESSÁRIO.
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {} - Idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    print('Erro de indice')
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado!!')