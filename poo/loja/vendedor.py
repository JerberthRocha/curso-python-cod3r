from .pessoa import Pessoa  # IMPORTAÇÃO DE FORMA RELATIVA


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init(nome, idade)
        self.salario = salario
