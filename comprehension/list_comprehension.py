# [ expressão for item in list if condicional ]
# LIST COMPREHENSION
dobros = [i * 2 for i in range(10)]
print(f'Lista gerada com List Comprehesion: {dobros}')

dobros = []
for i in range(10):
    dobros.append(i * 2)

print(f'Lista gerada do jeito tradicional: {dobros}')

dobros = [i * 2 for i in range(10) if i % 2 == 0]
print(dobros)