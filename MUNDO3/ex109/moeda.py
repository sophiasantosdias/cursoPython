import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def metade(p=0, format=True):
    met = p / 2
    if format:
        met = moeda(met)
    return met


def dobro(p=0, format=True):
    dobro = 2 * p
    if format:
        dobro = moeda(dobro)
    return dobro


def aumento(p=0, v=0, format=True):
    aum = p + p * v /100
    if format:
        aum = moeda(aum)
    return aum


def diminuicao(p=0, v=0, format=True):
    dim = p - p * v / 100
    if format:
        dim = moeda(dim)
    return dim


def moeda(p=0):
    str = f'R${locale.currency(p, grouping=True)}'
    return str
