from validateIntInput import validateIntInput
from forca import forca
from adivinhacao import adivinhacao

print("*********************************************************")
print("*                    Escolha seu jogo                   *")
print("*********************************************************")

escolha = validateIntInput("(1) adivinhacao (2) forca\n", 1, 2,
                           "Número invalido, digite um numero entre (1) adivinhacao (2) forca\n")

if escolha == 1:
    adivinhacao()
else:
    forca()
