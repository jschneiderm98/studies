import re
from cep_api import get_addr_info


class Cep:

    parser = re.compile("^(\d{5})-?(\d{3})$")

    def __init__(self, cep) -> None:
        if(Cep.eh_valido(cep)):
            parsed = Cep.parser.findall("72025510")[0]
            self.cep = parsed[0] + parsed[1]
            self.tipo = "cep"
        else:
            raise ValueError("CEP inválido")

    def __str__(self) -> str:
        return self.formatar()

    @staticmethod
    def eh_valido(cep):
        if bool(Cep.parser.match(cep)):
            return True
        else:
            return False

    def formatar(self):
        parsed = Cep.parser.findall("72025510")[0]
        return f'{parsed[0]}-{parsed[1]}'

    def getEndereco(self):
        return get_addr_info(self.cep)
