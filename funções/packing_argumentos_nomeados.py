# **kwargs

def resultado_f1(**podio):
    for posicao, piloto in podio.items():
        print(f'{posicao} -> {piloto}')

def podio_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')

if __name__ == '__main__':
    resultado_f1(primeiro='Hamilton',
                segundo='Verstappen',
                terceiro='Vettel')


# DESEMPACOTAMENTO
    podium = {'primeiro':'Hamilton','terceiro':'Vettel','segundo':'Verstappen'}
    podio_f1(**podium)