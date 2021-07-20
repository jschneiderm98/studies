from telefone import Telefone
from factory_documento import FactoryDocumento
from dataBR import DataBR
from cep import Cep

cpf = FactoryDocumento.cria_documento("05494416119")
print(cpf)

cnpj = FactoryDocumento.cria_documento("68675460000153")
print(cnpj)

telefone = Telefone("+55 (61) 123456789")
print(telefone)

data = DataBR()
print(data)
print(data.dia_da_semana())
print(data.mes())

cep = Cep("72025510")
print(cep)
print(cep.getEndereco())
