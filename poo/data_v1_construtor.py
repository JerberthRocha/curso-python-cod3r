class Data:
    def __init__(self, dia, mes, ano): #CONSTRUTOR: COMEÇA COM A PALAVRA RESERVADA __init__
        # PYTHON NÃO PERMITE MAIS DE UM CONSTRUTOR EM UMA MESMA CLASSE
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def to_str(self):  # TODOS OS MÉTODOS OBRIGATÓRIAMENTE COMEÇAM COM A PALAVRA RESERVADA self(REPRESENTA O OBJETO ATUAL)
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 11, 2022)  # ESTANCIAMENTO DA CLASSE DATA
print(d1.to_str())

d2 = Data(12, 12, 2012)  # ESTANCIAMENTO DA CLASSE DATA
print(d2.to_str())
