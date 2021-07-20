import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"
user = "Julio Cesar 054.944.161-19"
padrao = re.compile("[0-9]{5}-?[0-9]{3}")
cpfPattern = re.compile("([0-9]{3}[.]?){3}-?[0-9]{2}")
busca = padrao.search(endereco)

if busca:
    print(busca.group())

busca = cpfPattern.search(user)

if busca:
    print(busca.group())
