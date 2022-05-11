# TIRANDO CONFLITO DE NOMES DE MÓDULOS E FUNÇÕES
from pacote1 import modulo1
from pacote2 import modulo1 as modulo1_subtracao

print(f'Soma: {modulo1.soma(5, 6)}')
print(f'Subtração: {modulo1_subtracao.subtracao(7, 6)}')

