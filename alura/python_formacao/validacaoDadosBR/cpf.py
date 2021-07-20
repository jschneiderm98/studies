from validate_docbr import CPF


class Cpf:

    validator = CPF()

    def __init__(self, cpf) -> None:
        if(Cpf.eh_valido(cpf)):
            self.cpf = cpf
            self.tipo = "cpf"
        else:
            raise ValueError("CPF inválido")

    def __str__(self) -> str:
        return self.formatar()

    @staticmethod
    def eh_valido(cpf):
        if len(cpf) == 11 and Cpf.validator.validate(cpf):
            return True
        else:
            return False

    def formatar(self):
        return Cpf.validator.mask(self.cpf)
