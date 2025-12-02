import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def metade(p=0):
    met = p / 2
    return met


def dobro(p=0):
    dobro = 2 * p
    return dobro


def aumento(p=0, v):
    aum = p + p * v /100
    return aum


def diminuicao(p=0, v):
    dim = p - p * v / 100
    return dim


def moeda(p=0):
    str = f'R${locale.currency(p, grouping=True)}'
    return str
