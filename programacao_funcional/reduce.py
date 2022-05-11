from functools import reduce

pessoas =[
    {'nome':'Maria', 'idade':11},
    {'nome':'Mariana', 'idade':18},
    {'nome':'Ana', 'idade':26},
    {'nome':'José', 'idade':6},
    {'nome':'Jonas', 'idade':19},
    {'nome':'Gabriela', 'idade':17},
]

so_idades = map(lambda p: p['idade'],  pessoas)
menores = filter(lambda idade: idade < 18, so_idades)

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(f'Soma das idades: {soma_idades}')
soma_idades_menores = reduce(lambda idades, idade: idades + idade, menores, 0)
print(f'Soma das idades dos menores: {soma_idades_menores}')