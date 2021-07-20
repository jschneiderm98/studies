from ExtratorURL import ExtratorURL
from ConversorMoeda import Conversor
url = ExtratorURL(
    "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
url2 = ExtratorURL(
    "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
#url = ExtratorURL(None)
url.isValidURL()
print(url)
print(url == url2)
print(len(url))
print(url.getBase())
print(url.getParams())
params = url.getParsedParams()
print(params)

print(Conversor.convert(float(params["quantidade"]),
                        params["moedaOrigem"], params["moedaDestino"]))
