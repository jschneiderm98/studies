from cpf import Cpf
from cnpj import Cnpj


class FactoryDocumento():
    @staticmethod
    def cria_documento(doc):
        if(len(doc) == 11):
            return Cpf(doc)
        elif(len(doc) == 14):
            return Cnpj(doc)
        else:
            raise ValueError(
                "A quantidade de digitos informada não pode ser resolvida para um tipo de documento, 11-CPF 14-CNPJ")
