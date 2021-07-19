class Audiovisual:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    def darLike(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    def __str__(self) -> str:
        return f'{self.nome} - {self.ano} - {self.likes} likes'
