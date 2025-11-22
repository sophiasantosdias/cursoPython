# Matriz em Python

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for p, v in enumerate(matriz):
    for i, c in enumerate(matriz[p]):
        num = int(input(f'Digite um valor para [{p}, {i}]: '))
        matriz[p][i] = num

for p, v in enumerate(matriz):
    print(f'[{matriz[p][0]:^4}] [{matriz[p][1]:^4}] [{matriz[p][2]:^4}]')
