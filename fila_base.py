import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: list = []
    clientes_atendidos: list = []
    senha_atual: str = ""

    # constantes
    LIMITE_MAXIMO_FILA = 200
    LIMITE_MINIMO_FILA = 0
    CODIGO_FILA_NORMAL = 'NM'
    CODIGO_FILA_PRIORITARIA = 'PR'

    def reseta_fila(self) -> None:
        if self.codigo >= self.LIMITE_MAXIMO_FILA:
            self.codigo = self.LIMITE_MINIMO_FILA
        else:
            self.codigo += 1

    @abc.abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.adiciona_cliente_na_fila()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...

    def adiciona_cliente_na_fila(self):
        self.fila.append(self.senha_atual)
