from sys import getprofile
from validadorURL import validaURL


class ExtratorURL:
    def __init__(self, url) -> None:
        self.url = self.__sanitizeURL(url) if type(url) == str else ""

    def __len__(self) -> str:
        return len(self.url)

    def __str__(self) -> str:
        return self.url + "\nbase: " + self.getBase() + "\nparametros: " + str(self.getParsedParams())

    def __eq__(self, o: object) -> bool:
        return self.url == o.url

    def __sanitizeURL(_self, url):
        return url.replace(" ", "").strip()

    def isValidURL(self):
        if not self.url:
            raise ValueError("URL vazia")
        if not validaURL(self.url):
            raise ValueError("URL inválida")
        return True

    def getBase(self):
        return self.url.split("//")[1].split("?")[0]

    def getParams(self):
        return self.url.split("//")[1].split("?")[1].split("&")

    def getParsedParams(self):
        params = {}
        [params.update({param.split("=")[0]: param.split("=")[1]})
         for param in self.getParams()]
        return params
