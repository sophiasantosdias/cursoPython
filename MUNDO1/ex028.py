# Jogo da Adivinhação v.1.0
from random import randint
print('====== DESAFIO 28 ======')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = randint(0, 5)
chute = int(input('Em que número eu pensei? '))
if chute == num:
    print('VOCÊ ME GANHOU!!')
else:
    print('ERROU!! O número que pensei foi {} e não {}.'.format(num, chute))
