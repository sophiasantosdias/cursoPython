# Sortear e Somar
from random import randint

numeros = []

def sortear(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
    for i, v in enumerate(lista):
        print(v, end=' ')
    print()


def somaPar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lst}, temos {soma}')


sortear(numeros)
somaPar(numeros)
