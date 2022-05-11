def soma_2(a, b):
    return a + b

def soma_3(a, b, c):
    return a + b + c

# EMPACOTAMENTO
def soma_n(*numeros): # QUANTIDADE DE PARAMETROS INDEFINIDOS. 'numeros' SE TORNA UMA TUPLA POR CAUSA DO ASTERISCO
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

if __name__ == '__main__':
    print(soma_2(1, 2))
    print(soma_3(1, 2, 3))
    print(soma_n(1, 2, 3, 4, 5))

    # DESEMPACOTAMENTO
    lista_numeros = [1, 2, 3]
    print(soma_3(*lista_numeros)) # O ASTERISCO FAZ O DESEMPACOTAMENTO DOS ARGUMENTOS. PODE SER TUPLA, LISTA...