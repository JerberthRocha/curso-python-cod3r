from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# PORTUGUÊS DO BRASIL
setlocale(LC_ALL, 'pt_BR')

# 1 - (FILTER) PEGAR OS INDICES DE TODOS OS MESES COM 31 DIAS
# 2 - (MAP) TRANSFORMAR OS INDICES EM NOMES
# 3 - (REDUCE) JUNTAR TUDO PARA IMPRIMIR

# LISTAR TODOS OS MESES DO ANO QUE TEM 31 DIAS
# meses_com_31_dias = filter(lambda mdays: len(mdays) == 31, mdays)
# print(list(meses_com_31_dias))
# meses_com_31_dias = []
# i = 0
# for d in mdays:
#     if d == 31:
#         meses_com_31_dias.append(month_name[i])
#     i += 1
# print(f'Meses com 31 dias: {meses_com_31_dias}')

meses_com_31_dias = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nomes = map(lambda mes: month_name[mes], meses_com_31_dias)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                      meses_nomes, 'Meses com 31 dias:')

print(juntar_meses)
