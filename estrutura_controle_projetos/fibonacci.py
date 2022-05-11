# 0, 1, 1, 2, 3, 5, 8...

# def fibonacci(limite):
#     penultimo = 0
#     ultimo = 1
#     print(f'{penultimo}, {ultimo}', end=', ')
#     while ultimo < limite:
#         # USANDO UMA VARIÁVEL AUXILIAR PARA TROCA DE VALORES DAS VARIÁVEIS
#         proximo = ultimo + penultimo
#         print(f'{proximo}', end=',')
#         penultimo = ultimo
#         ultimo = proximo


# def fibonacci(limite):
#     penultimo = 0
#     ultimo = 1
#     print(f'{penultimo}, {ultimo}', end=', ')
#     while ultimo < limite:
#         # USANDO PACKING PARA TROCA DOS VALORES DAS VARIÁVEIS
#         penultimo, ultimo = ultimo, penultimo + ultimo
#         print(f'{ultimo}', end=', ')


def fibonacci(quantidade):
    resultado = [0, 1]
    while len(resultado) < quantidade:
        # resultado.append(resultado[-2] + resultado[-1])
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for elemento in fibonacci(20):
        print(elemento, end=', ')
