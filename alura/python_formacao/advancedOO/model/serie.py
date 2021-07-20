from model.audiovisual import Audiovisual


class Serie(Audiovisual):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self) -> str:
        return super().__str__() + f' - {self.temporadas} temporadas'
