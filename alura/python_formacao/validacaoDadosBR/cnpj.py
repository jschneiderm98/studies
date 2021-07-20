import re
from validate_docbr import CNPJ


class Cnpj:

    validator = CNPJ()

    def __init__(self, cnpj) -> None:
        if(Cnpj.eh_valido(cnpj)):
            self.cnpj = cnpj
            self.tipo = "cnpj"
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self) -> str:
        return self.formatar()

    @staticmethod
    def eh_valido(cnpj):
        if len(cnpj) == 14 and Cnpj.validator.validate(cnpj):
            return True
        else:
            return False

    def formatar(self):
        return Cnpj.validator.mask(self.cnpj)
