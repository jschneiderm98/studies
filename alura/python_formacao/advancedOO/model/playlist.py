class Playlist:
    def __init__(self, nome, programas=[]) -> None:
        self.__programas = programas
        self.nome = nome

    def add(self, value):
        self.__programas.append(value)

    def __getitem__(self, item):
        return self.__programas[item]

    def __len__(self):
        return len(self.__programas)

    @property
    def listagem(self):
        return self.__programas

    @property
    def tamanho(self):
        return len(self.__programas)
