import requests


def get_addr_info(cep):
    r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if (r.status_code == 200):
        return (True, r.json())
    return (False, "Failed request")
