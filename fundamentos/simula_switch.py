# A FUNÇÃO SWITCH NÃO EXISTE NATIVAMENTE NO PYTHON
# USANDO FUNÇÃO E DICIONÁRIO PARA SIMULAR O SWITCH

def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }
    return dias.get(dia, '=*=* DIA INVÁLIDO *=*=')

if __name__ == '__main__':
    for dia in range(9):
        if dia == 1 or dia == 7:
            print(f'{dia} -> {get_dia_semana(dia)} -> Final de semana')
        if 2<= dia <=6:
            print(f'{dia} -> {get_dia_semana(dia)} -> Dia Útil')
        if dia <= 0 or dia > 7:
            print(f'{dia}: =*=* DIA INVÁLIDO *=*=')

