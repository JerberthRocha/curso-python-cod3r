class Data:
    # pass # DIZ QUE O BLOCO ASSOCIADO A ESSA CLASSE É UM BLOCO VAZIO. O MESMO VALE PARA FUNÇÕES
    def to_str(self): # TODOS OS MÉTODOS OBRIGATÓRIAMENTE COMEÇAM COM A PALAVRA RESERVADA self
        return f'{self.dia}/{self.mes}/{self.ano}'

d1 = Data() # ESTANCIAMENTO DA CLASSE DATA
d1.dia = 5
d1.mes = 11
d1.ano = 2022

# print(f'{d1.dia}/{d1.mes}/{d1.ano}')
# print(type(d1))
print(d1.to_str())

d2 = Data() # ESTANCIAMENTO DA CLASSE DATA
d2.dia = 12
d2.mes = 12
d2.ano = 2012

print(d2.to_str())