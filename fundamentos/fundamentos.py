# # #Tipos básicos
# # print(True)
# # print(False)
# # print(1.2 + 1)
# # print('Isso eh uma string')
# # print(f'Lista -> {[1, 2, 3]}')
# # print(f"Dicionario -> {{'nome':'maria', 'idade': 22}}")
# # print(f'Tupla -> {(1, 2, 3, 4, 5)}')
# # print(None) # equivalente a null/default em outras linguagens


# # salario = 3450.45
# # despesas = 2456.2

# # percentual_comprometido = despesas * 100 / salario

# # print(percentual_comprometido)

# ###### OPERAÇÕES BIT A BIT ######
# # AND
# # 3 = 11
# # 2 = 10
# # _ = 10 -> 2 EM BINÁRIO
# from re import X


# print(3 & 2)


# # OR
# # 3 = 11
# # 2 = 10
# # _ = 11 -> 3 EM BINÁRIO
# print(3 | 2)

# # XOR
# # 3 = 11
# # 2 = 10
# # _ = 01 -> 1 EM BINÁRIO
# print(3 ^ 2)


# saldo = 1000
# salario = 4000
# despesas = 2900

# saldo_positivo = saldo > 0
# despesas_controladas = salario - despesas >= 0.2 * salario

# meta = saldo_positivo and despesas_controladas
# print(meta)

# # OPERADORES TERNÁRIOS
# esta_chovendo = False
# print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo]) # OPERADOR TERNÁRIO. QUANDO VERDADEIRO O VALOR IMPRESSO SERÁ O MAIS PRÓXIMO DA EXPRESSÃO. VALOR MAIS PRÓXIMO DA EXPRESSÃO = A TRUE
# print('Hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.'))

# # OPERADOR DE MEMBRO
# lista = [1, 2, 3, 'Maria', 'Jose']
# print('Jose' in lista)
# print('Jose' not in lista)

# # OPERADOR DE IDENTIDADE
# x = 3
# y = x
# z = 3

# print(x is z) # True pq os valores são iguais

# lista1 = [1,2,3]
# lista2 = lista1
# lista3 = [1,2,3]
# lista1.append(4)

# print(lista2)

# BUILTINS
# funções que são disponibilizadas pelo módulo builtins
# - type
# - print
# - help
# - dir
# - len

# frase = 'Python é uma linguagem excelente'

# print('py' in frase)
# print('exc' in frase)

lista =  list()
# lista.append(1)
# lista.append(2)
# print(lista)
# lista.reverse()
# print(lista)
# lista.append(9)
# print(lista)
print(dir(lista))