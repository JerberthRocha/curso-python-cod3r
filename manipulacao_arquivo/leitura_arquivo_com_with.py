#A FUNÇÃO WITH FECHA O ARQUIVO AUTOMATICAMENTE

with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome:{} - Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo fechado!') 