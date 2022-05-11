from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # CONCEITO DE SOBRECARGA DE OPERADOR
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    # MÉTODOS QUE INICIAM COM _ SÃO MÉTODOS PRIVADOS
    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        # CONCEITO DE SOBRECARGA
        # VERIFICA SE tarefa É UMA INSTANCIA DE Tarefa
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        try:
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0]
        except IndexError as e:  # O IDEAL É TRATAR AS EXCEÇÕES DA FORMA MAIS ESPECÍFICA POSSÍVEL
            raise TarefaNaoEncontrada(str(e))

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append(' (Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append(' (Vencida)')
            else:
                # PEGA A DIFERENÇA DE DIAS GERADA PELA SUBTRAÇÃO ENTRE DAS DATAS
                dias = (self.vencimento - datetime.now()).days
                status.append(f' (Vence em {dias} dias)')
        return f'{self.descricao}' + ' '.join(status)


# CONCEITO DE HERANÇA. CLASSE TAREFA É PAI(SUPERCLASSE) DA CLASSE TAREFARECORRENTE(FILHA/SUBCLASSE)
class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de Casa:')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar pratos')
    # SOBRECARGA DE OPERADOR
    casa += TarefaRecorrente('Trocar lençóis', datetime.now(), 7)
    casa.procurar('Trocar lençóis').concluir()
    print(casa)

    try:
        casa.procurar('Lavar prato - ERRO').concluir()
    except TarefaNaoEncontrada as e:
        print(f'A causa do erro foi: "{str(e)}"!')

    casa.procurar('Lavar pratos').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compas no mercado:')
    mercado.add('Frutas')
    mercado.add('Carne')
    mercado.add('Peixe', datetime.now() + timedelta(days=3, minutes=22))
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
