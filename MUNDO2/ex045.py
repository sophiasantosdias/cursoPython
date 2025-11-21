import random
from time import sleep
# Pedra, Papel e Tesoura
print('====== DESAFIO 45 ======')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = int(input('Qual a sua jogada? '))
computador = random.randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHA')
    elif jogador == 2:
        print('COMPUTADOR GANHA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHA')
    elif jogador == 1:
        print('COMPUTADOR GANHA')
    elif jogador == 2:
        print('EMPATE')
