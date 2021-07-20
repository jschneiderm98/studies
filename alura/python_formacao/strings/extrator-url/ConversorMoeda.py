class Conversor:
    moedas = {
        "real": 1,
        "dolar": 5.11,
        "euro": 6.04,
        "libraEsterlina": 7.07
    }

    @staticmethod
    def convert(value, origin, target):
        print(value)
        print(Conversor.moedas[target])
        print(Conversor.moedas[origin])
        return value * (Conversor.moedas[target] / Conversor.moedas[origin])
