import sys

generator = (i ** 2 for i in range(10) if i % 2 == 0)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# a = (i ** 2 for i in range(1000) if i % 2 == 0)
# b = [i ** 2 for i in range(1000) if i % 2 == 0]
# print('\n')
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

for numero in generator:
    print(numero)