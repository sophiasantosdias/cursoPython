# Jogo da Adivinhação v2.0
print('====== DESAFIO 58 ======')
from random import randint
num = randint(0, 10)
t = 0
tentativa = -1

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

while tentativa != num:
    tentativa = int(input('Digite seu palpite: '))
    t += 1
    if tentativa > num:
        print('Menos... Tente outra vez.')
    elif tentativa < num:
        print('Mais... Tente outra vez.')

print('Parábens! Você Acertou!')
print('Você precisou de {} tentativas'.format(t))

