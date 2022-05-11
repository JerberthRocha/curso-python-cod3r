# def imprimir(maximo, atual):
#     if maximo < atual:
#         return
#     print(atual)
#     imprimir(maximo, atual + 1)

# imprimir(10, 1)


def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for elemento in fibonacci(20):
        print(elemento)