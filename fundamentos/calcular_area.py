from math import pi
from re import A


# class cores_terminal:
#     normal = '\033[91m'
#     erro = '\033[0m'


def valor_invalido():
    print('Valor Inválido.')


def circulo(raio):
    return pi * raio ** 2


if __name__ == '__main__':  # VERIFICA SE ESTÁ NO MÓDULO __main__
    raio = input('Informe o valor do raio: ')
    if raio.isnumeric():
        raio = float(raio)
        circulo(raio)
        area = circulo(raio)
        print(f'Área = {area}')
    else:
        valor_invalido()


# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
