# UMA FUNÇÃO SENDO ARMAZENADA EM UMA VARIÁVEL É O CONCEITO DE FUNÇÃO DE PRIMEIRA CLASSE
# UMA FUNÇÃO QUE RETORNA UMA FUNÇÃO É UMA FUNÇÃO DE ALTA ORDEM
# PASSAR OS PARAMETROS PARCIALMENTE E ELES SÓ SEREM AVALIADOS QUANDO O ÚLTIMO SER PASSADO É O CONCEITO DE AVALIAÇÃO TARDIA

def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro)
    print(triplo)
    print(f'O dobro de 7 é {dobro(7)}')
    print(f'O triplo de 3 é {triplo(3)}')