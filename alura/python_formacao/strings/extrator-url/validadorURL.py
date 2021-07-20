import re


def validaURL(url):
    test = re.match("^(https?://)?(www)?\w+(.\w+)+/?(\w+/?)?$", url)
    return (url == test.group()) if test else False
