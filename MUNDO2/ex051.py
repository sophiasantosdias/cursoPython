# Progressão Aritmética
print('====== DESAFIO 51 ======')
n1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
for c in range(n1, n1 + (r * 10), r):
    print(c, end=' -> ')
print('ACABOU')
