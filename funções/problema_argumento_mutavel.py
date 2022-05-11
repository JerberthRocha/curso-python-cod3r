# def fibonacci(sequencia=[0, 1]):
#     # USO DE ARGUMENTOS MUTÁVEIS COMO VALOR DEFAULT PODE CAUSAR PROBLEMAS
#     sequencia.append(sequencia[-1] + sequencia[-2])
#     return sequencia


# if __name__ == '__main__':
#     inicio = fibonacci()
#     print(inicio, id(inicio))
#     print(fibonacci(inicio))
#     restart = fibonacci()
#     print(restart, id(restart))

#CORREÇÃO 

def fibonacci(sequencia=None):
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
