# Sorteio de um item na lista
from random import choice
print('====== DESAFIO 19 ======')
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
lista = [al1, al2, al3, al4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
