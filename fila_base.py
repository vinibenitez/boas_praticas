import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: list = []
    clientes_atendidos: list = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
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
