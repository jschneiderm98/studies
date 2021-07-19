from datetime import datetime, timedelta
from datasBRHelper import meses, dias_semana


class DataBR:
    def __init__(self, data=None) -> None:
        if(not data):
            data = datetime.today()
        self.__data = data

    def __str__(self) -> str:
        return self.format()

    def mes(self):
        return meses[self.__data.month-1]

    def dia_da_semana(self):
        return dias_semana[self.__data.weekday()]

    def format(self):
        return self.__data.strftime("%d/%m/%Y %H:%M")
