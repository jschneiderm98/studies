class Conta:
    def __init__(self, numero, titular, saldo, limite) -> None:
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        return valor < (self.__saldo + self.__limite)

    def sacar(self, valor):
        if not self.__pode_sacar(valor):
            print("valor maior que o saldo")
            return
        self.__saldo -= valor

    def gerarExtrato(self):
        print("O saldo do titular {} é {}".format(self.__titular, self.__saldo))

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

    def depositar(self, origem, valor):
        origem.sacar(valor)
        self.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def codigo_banco():
        return "001"

    @limite.setter
    def limite(self, valor):
        self.__limite = valor
