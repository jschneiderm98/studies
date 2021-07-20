from model.serie import Serie
from model.filme import Filme
from model.playlist import Playlist

serie = Serie("Breaking Bad", 2011, 7)
serie2 = Serie("Twin Peaks", 1997, 3)
filme = Filme("Natura", 2000, 170)
filme2 = Filme("Teste", 2021, 130)
filme3 = Filme("Azul", 2000, 165)
playlist = Playlist("Quero assistir")

playlist.add(serie)
playlist.add(serie2)
playlist.add(filme)
playlist.add(filme2)
playlist.add(filme3)

serie.darLike()
serie.darLike()
serie2.darLike()

filme.darLike()
filme2.darLike()
filme2.darLike()
filme3.darLike()

print('Tamanho da playlist:', len(playlist))

for programa in playlist:
    print(programa)

print(serie2 in playlist)
