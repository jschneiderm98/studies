from model.audiovisual import Audiovisual


class Filme(Audiovisual):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self) -> str:
        return super().__str__() + f' - {self.duracao} min'
