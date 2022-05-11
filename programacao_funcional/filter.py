pessoas =[
    {'nome':'Maria', 'idade':11},
    {'nome':'Mariana', 'idade':18},
    {'nome':'Ana', 'idade':26},
    {'nome':'José', 'idade':6},
    {'nome':'Jonas', 'idade':19},
    {'nome':'Gabriela', 'idade':17},
]

menores = filter(lambda p: p['idade'] < 18, pessoas) # O LAMBDA QUE É PASSADA PARA A FUNÇÃO FILTER SEMPRE VAI RETORNAR VERDADEIRO OU FALSO
print(list(menores))
nomes_grandes = filter(lambda p: len(p['nome']) >= 6, pessoas)
print(tuple(nomes_grandes))