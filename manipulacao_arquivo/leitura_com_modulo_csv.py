import csv
#ASTERISCO(*) = OPERADOR DE ARGUMENTOS VARIÁVEIS
with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))