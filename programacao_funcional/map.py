lista_1 = [1, 2, 3]

dobro = map(lambda x: x * 2, lista_1)

print(list(dobro))

lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26},
]

nomes = map(lambda p: p['nome'], lista_2)
print(list(nomes))
idade = map(lambda p: p['idade'], lista_2)
print(list(idade))

dados = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista_2)
print(list(dados))