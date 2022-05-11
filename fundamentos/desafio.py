from operator import imod
from random import randint


def dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 != 0:
        continue
    else:
        numero = dado()
        if i == numero:
            print(f'O número sorteado foi {numero} - Você escolheu o numero {i}. PARABÉNS, VOCÊ ACERTOU!!!')
            break
else:
    print(f'O número sorteado foi {numero} - Você escolheu o numero {i}. NÃO ACERTOU O NÚMERO.')
