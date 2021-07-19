import random
import visaoForca


def init():
    firstMessage()
    return (7, False, False, set(), 0, "")


def getSecretWord(file):
    with open(file, 'r') as arquivo:
        palavras = arquivo.read().split('\n')
    return random.choice(palavras).lower()


def firstMessage():
    print("*********************************************************")
    print("*               Bem vindo ao jogo da forca              *")
    print("*********************************************************")


def formKnownWord(palavra_secreta, ocorrencias):
    palavra_conhecida = ""
    for letra in palavra_secreta:
        if(letra in ocorrencias):
            palavra_conhecida = palavra_conhecida + letra
        else:
            palavra_conhecida = palavra_conhecida + "_"
    return palavra_conhecida


def forca():

    palavra_secreta = getSecretWord('palavras.txt')

    (vidas, enforcou, acertou, ocorrencias, erros, palavra_conhecida) = init()

    while(not enforcou and not acertou):

        print("Letras conhecidas até agora:", palavra_conhecida)
        chute = input("Digite uma letra para adivinhar\n").lower().strip()

        if chute in palavra_secreta:
            [ocorrencias.add(letra)
             for letra in palavra_secreta if(chute == letra)]
        else:
            erros += 1
            visaoForca.desenha_forca(erros)

        enforcou = erros == vidas

        palavra_conhecida = formKnownWord(palavra_secreta, ocorrencias)

        acertou = palavra_conhecida == palavra_secreta

    if(acertou):
        visaoForca.imprime_mensagem_vencedor()
    else:
        visaoForca.imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo")


if __name__ == "__main__":
    forca()
