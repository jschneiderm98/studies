import random
from validateIntInput import validateIntInput


def adivinhacao():
    print("********************************************************")
    print("*           Bem vindo ao jogo de adivinhação           *")
    print("********************************************************")

    hidden_num = random.randint(1, 100)
    pontos = 1000
    print(hidden_num)

    print("Qual nível de dificuldade?")
    dificuldade = validateIntInput("1 - fácil, 2 - médio, 3 - difícil\n", 1, 3,
                                   "Número invalido, digite um numero entre 1 e 3\n")
    vidas = 0
    if (dificuldade == 1):
        vidas = 20
    elif (dificuldade == 2):
        vidas = 10
    else:
        vidas = 5

    for rodada in range(vidas):
        print("Tentativa {} de {}".format(rodada+1, vidas))
        escolha = validateIntInput("Digite um número entre 1 e 100\n", 1, 100,
                                   "Número invalido, digite um numero entre 1 e 100\n")

        print("Você digitou", escolha)

        if (escolha == hidden_num):
            print("Você acertou")
            break
        elif(escolha > hidden_num):
            print("Você errou, seu chute foi muito alto")
            pontos = pontos - (escolha - hidden_num)
            print(pontos)
        else:
            print("Você errou, seu chute foi muito baixo")
            pontos = pontos - (hidden_num - escolha)
            print(pontos)

    print("Fim do jogo")
    print(f"Você fez {pontos} pontos")


if (__name__ == "__main__"):
    adivinhacao()
