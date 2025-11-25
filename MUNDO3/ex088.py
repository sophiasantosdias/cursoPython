# Palpites para Mega Sena
import random

print('-'*30)
print(f'{'JOGAR NA MEGA SENA':^30}')
print('-'*30)

jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie: '))
q = 0
sorteado = 0
jogo = []

print('-=-'*3, end=' ')
print(f'SORTEANDO {quant} JOGOS', end=' ');
print('-=-'*3)

for i in range (1, quant + 1):
    while len(jogo) < 6:
        sorteado = random.randint(1, 60)
        if sorteado not in jogo:
            jogo.append(sorteado)
    jogos.append(jogo[:])
    jogo.clear()

for i, j in enumerate(jogos):
    print(f'Jogo {i + 1}: {j}')
