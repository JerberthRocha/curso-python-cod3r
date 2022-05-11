class Animal:
    @property
    def capacidades(self):
        return('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'Andar pelas paredes')


class SpiderMan(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'atiras teias', 'sentido aranha')


if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidades}')

    dona_aranha = Aranha()
    print(f'Dona Aranha: {dona_aranha.capacidades}')

    peter = SpiderMan()
    print(f'Peter Parker: {peter.capacidades}')
