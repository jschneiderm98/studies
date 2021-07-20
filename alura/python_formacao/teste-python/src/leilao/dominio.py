from src.leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor):
        if not self.__valor_eh_valido(valor):
            raise LanceInvalido(
                "O usuário não tem dinheiro na carteira para dar esse lance")
        leilao.propoe(Lance(self, valor))
        self.__carteira -= valor

    def __valor_eh_valido(self, valor):
        return self.__carteira >= valor


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def __tem_lances(self):
        return bool(self.__lances)

    def __sao_usuarios_diferentes(self, usuario: Usuario):
        if self.ultimo_lance.usuario != usuario:
            return True
        else:
            raise LanceInvalido(
                "O mesmo usuário não pode realizar dois lances seguidos")

    def __eh_maior_que_lance_anterior(self, valor):
        if valor > self.__lances[-1].valor:
            return True
        else:
            raise LanceInvalido("Erro ao propor o lance")

    def __lance_eh_valido(self, lance: Lance):
        return not self.__lances or (self.__sao_usuarios_diferentes(lance.usuario) and
                                     self.__eh_maior_que_lance_anterior(lance.valor))

    def propoe(self, lance: Lance):
        self.__lance_eh_valido(lance)
        self.ultimo_lance = lance
        if not self.__tem_lances():
            self.menor_lance = lance.valor
        self.maior_lance = lance.valor

        self.__lances.append(lance)
