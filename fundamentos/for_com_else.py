PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'O Milan vai ganhar o scudetto da temporada 2021-2022',
    'Botafogo de F . R.',
    'A praia foi divertida'
]

textos_validos = []

for texto in textos:
    interseção = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if interseção:
        print(f'O texto contém palavra(s) proibida(s) -> {interseção}')
    else:
        print(f'Texto válido: {texto}')


# PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
# textos = [
#     'João gosta de futebol e política',
#     'O Milan vai ganhar o scudetto da temporada 2021-2022',
#     'Botafogo de F . R.'
# ]

# textos_validos = []

# for texto in textos:
#     for palavra in texto.lower().split():
#         if palavra in PALAVRAS_PROIBIDAS:
#             print(f'O texto contém pelo menos uma palavra proibida -> {palavra}')
#             break
#     else:
#         textos_validos.append(texto)

# for texto in textos_validos:
#     print(texto)
