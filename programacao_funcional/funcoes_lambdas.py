# a = [1, 2, 3]
# dobro = map(lambda i: i * 2, a)
# print(a)
# print(list(dobro))

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'], compras
    )
)

print('Preços totais:', totais)
print('Total geral: R$', sum(totais))
