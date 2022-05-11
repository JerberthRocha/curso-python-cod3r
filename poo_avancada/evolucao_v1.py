class Humano:
    especie = 'Homo Sapiens' # ATRIBUTO DE CLASSE. ÚNICO VALOR PARA TODAS AS INSTANCIAS FEITAS

    def __init__(self, nome):
        self.nome = nome # ATRIBUTO DE INSTANCIA

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self # RETORNO O OBJETO
# EM PYTHON, MÉTODOS SEM return RETORNAM None POR PADRÃO

if __name__ == '__main__':
    jose = Humano('José')
    grok = Humano('Grok').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grok.especie: {grok.especie}')
