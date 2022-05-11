# CONJUNTOS OU SET
conjunto = {1, 2, 3, 7, 8, 9}
print(type(conjunto))
# print(conjunto[0]) #SET NÃO É INDEXADO
conjunto = set('python')
print(conjunto)
print(2 in conjunto, 'p' in conjunto)
conjunto = {1, 2, 3}
print(conjunto == {1, 1, 3, 3, 3, 3, 2, 2, 2})
a = {1, 2, 4, 6}
b = {2, 3, 4, 5}
# JUNTA OS 2 CONJUNTOS IGNORANDO OS REPETIDOS. NÃO ALTERA O CONJUNTO A
print(a.union(b))
# PEGA SOMENTE OS VALORES QUE EXISTE NOS 2 CONJUNTOS. NÃO ALTERA O CONJUNTO A
print(a.intersection(b))
# VERIFICA SE ALGUM VALOR DO CONJUNTO A EXSTE NO CONJUNTO B
# PEGA OS VALORES QUE EXISTEM EM A E QUE NÃO EXISTEM NO CONJUNTO B. NÃO ALTERA O CONJUNTO A
print(a - b)
a -= {6}  # REMOVE DO CONJUNTO VALOR ESPECIFICADO
print(a)
a.update(b)  # MODIFICA O CONJUNTO A
print(a)
print((b <= a))  # B É SUBCONJUNTO DE A?
print((a >= b))  # A É SUPERCONJUNTO DE B?
print(dir(conjunto))

