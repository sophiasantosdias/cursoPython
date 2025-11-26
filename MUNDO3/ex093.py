# Cadastro de Jogador
from time import sleep

jogador = {}
gols = []
soma = 0

jogador['nome'] = input('Nome do Jogador: ')
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(1, quant+1):
    gol = int(input(f'   Quantos gols na partida {i}? '))
    gols.append(gol)
    soma += gol

jogador['gols'] = gols[:]
jogador['total'] = soma

print(f'{" PRINT 1 ":=^60}')
print()
print(jogador)
print()

print(f'{" PRINT 2 ":=^60}')
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
    sleep(0.5)
print()

print(f'{" PRINT 3 ":=^60}')
print()
print(f'O Jogador {jogador["nome"]} jogou {quant} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i + 1*}, fez {v} gols.')
    sleep(0.5)
print(f'Foi um total de {soma} gols.')

