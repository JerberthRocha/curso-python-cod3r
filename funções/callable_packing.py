# PARAMETRO *ARGS
# def calc_preco_final(preco_bruto, calc_imposto, *params):
#     return preco_bruto + preco_bruto * calc_imposto(*params)


# def imposto_x(importado):
#     return 0.22 if importado else 0.13


# def imposto_y(explosivo, fator_multi=1):
#     return 0.11 * fator_multi if explosivo else 0


# if __name__ == '__main__':
#     preco_bruto = 134.98
#     preco_final = calc_preco_final(preco_bruto, imposto_x, True)
#     preco_final = calc_preco_final(preco_final, imposto_y, True, 1.5)
#     print(f'Preço final R${preco_final}')


# PARAMETRO **KWARGS
# def calc_preco_final(preco_bruto, calc_imposto, **params):
#     return preco_bruto + preco_bruto * calc_imposto(**params)


# def imposto_x(importado):
#     return 0.22 if importado else 0.13


# def imposto_y(explosivo, fator_multi=1):
#     return 0.11 * fator_multi if explosivo else 0


# if __name__ == '__main__':
#     preco_bruto = 134.98
#     preco_final = calc_preco_final(preco_bruto, imposto_x, importado=True)
#     preco_final = calc_preco_final(preco_final, imposto_y, explosivo=True, fator_multi=1.5)
#     print(f'Preço final R${preco_final}')


# PARAMETROS *ARGS E **KWARGS
def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')



if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)