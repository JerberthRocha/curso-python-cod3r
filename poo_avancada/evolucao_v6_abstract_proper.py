# MÉTODO DE INSTANCIA: RECEBE A INSTANCIA COMO PRIMEIRO PARAMETRO
# MÉTODO DE CLASSE: RECEBE A CLASSE COMO PRIMEIRO PARAMETRO
# MÉTODO ESTÁTICO: NÃO RECEBE PARAMETRO NA DEFINIÇÃO DO MÉTODO
# CLASSE ABSTRATA: UMA CLASSE QUE PELO MENOS UM DOS MÉTODOS NÃO ESTÁ IMPLEMENTADO
from abc import ABCMeta, abstractproperty


class Humano(metaclass=ABCMeta): # metaclass=ABCMeta SIGNIFICA QUE Humano PASSOU A SER UMA CLASSE ABSTRATA; ELA NÃO PODER SER INSTACIADA
    # ATRIBUTO DE CLASSE. ÚNICO VALOR PARA TODAS AS INSTANCIAS FEITAS
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome  # ATRIBUTO DE INSTANCIA
        self._idade = None

    @abstractproperty
    def inteligente(self):
        pass


    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um valor positivo!')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self  # RETORNO O OBJETO
# EM PYTHON, MÉTODOS SEM return RETORNAM None POR PADRÃO

    @staticmethod  # MÉTODO ESTÁTICO
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod  # MÉTODO DE CLASSE
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True

if __name__ == '__main__':

    try:
        anonimo = Humano('John')
        print(anonimo.inteligente)
    except TypeError:
        print('Classe Abstrata')

    jose = HomoSapiens('Grok')
    print(f'{jose.nome} da classe {jose.__class__.__name__}, Inteligente: {jose.inteligente}')
    grok = Neanderthal('Grok')
    print(f'{grok.nome} da classe {grok.__class__.__name__}, Inteligente: {grok.inteligente}')

