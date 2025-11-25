# Jogo de Dados
from random import randint
from time import sleep
from operator import itemgetter

jogadas = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
ranking = []

for k in jogadas.keys():
    jogadas[k] = randint(1, 6)

print('Os valores sorteados foram: ')
for j, n in jogadas.items():
    print(f'{j} tirou {n} no dado')
    sleep(1)
print('-' * 30)

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos')
    sleep(1)
