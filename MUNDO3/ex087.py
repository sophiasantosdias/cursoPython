# Matriz v2.0 em Python

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0
maior = 0
somaT = 0

for p, v in enumerate(matriz):
    for i, c in enumerate(matriz[p]):
        num = int(input(f'Digite um valor para [{p}, {i}]: '))
        matriz[p][i] = num
        if num % 2 == 0:
            somaPar += num

for p, v in enumerate(matriz):
    print(f'[{matriz[p][0]:^4}] [{matriz[p][1]:^4}] [{matriz[p][2]:^4}]')

for k in range(0, 3):
    somaT += matriz[k][2]
    maior = sorted(matriz[1])[-1]

print(f'A soma dos pares os valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaT}')
print(f'O maior valor da segunda linha é {maior}')
