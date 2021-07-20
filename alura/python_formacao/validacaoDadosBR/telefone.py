import re


class Telefone:
    parser = re.compile(
        "^(\+?\d{2})?\s*(\(?\d{2}\)?)?\s*(\d{4,5})-?(\d{4})$")

    def __init__(self, telefone) -> None:
        if(Telefone.eh_valido(telefone)):
            self.telefone = telefone
            self.tipo = "telefone"
        else:
            raise ValueError("Telefone inválido")

    def __str__(self) -> str:
        return self.formatar()

    @staticmethod
    def eh_valido(telefone):
        if bool(Telefone.parser.match(telefone)):
            return True
        else:
            return False

    def formatar(self):
        parts = Telefone.parser.findall(self.telefone)[0]
        print(parts)
        if(len(parts[0]) != 0 and len(parts[1]) != 0):
            countryNum = parts[0].replace('+', "")
            ddd = parts[1].replace('(', "").replace(')', "")
            return f'+{countryNum} ({ddd}) {parts[2]}-{parts[3]}'
        elif(len(parts[1]) != 0):
            ddd = parts[1].replace('(', "").replace(')', "")
            return f'({ddd}) {parts[2]}{parts[3]}'
        return f'{parts[2]}-{parts[3]}'
