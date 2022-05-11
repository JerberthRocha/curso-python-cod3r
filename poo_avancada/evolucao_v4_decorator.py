# MÉTODO DE INSTANCIA: RECEBE A INSTANCIA COMO PRIMEIRO PARAMETRO
# MÉTODO DE CLASSE: RECEBE A CLASSE COMO PRIMEIRO PARAMETRO
# MÉTODO ESTÁTICO: NÃO RECEBE PARAMETRO NA DEFINIÇÃO DO MÉTODO

class Humano:
    # ATRIBUTO DE CLASSE. ÚNICO VALOR PARA TODAS AS INSTANCIAS FEITAS
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome  # ATRIBUTO DE INSTANCIA
        self._idade = None

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


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.idade = 40
    print(f'Nome: {jose.nome} Idade: {jose.idade}')
