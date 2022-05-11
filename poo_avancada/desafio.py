class ClasseSimples:
    contador = 0
    
    def __init__(self): # SEMPRE QUE CONSTRUTOR É CHAMADO ELE CHAMA O MÉTODO DA CLASSE(contar)
        # self.__class__.contador += 1
        self.contar()

    @classmethod # MÉTODO DA CLASSE
    def contar(cls):
        cls.contador += 1

        

if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples(), ClasseSimples()]
    print(f'Quantidade: {ClasseSimples.contador}')