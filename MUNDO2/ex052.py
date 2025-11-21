# Números Primos
print('====== DESAFIO 52 ======')
num = int(input('Digite um número: '))
q = 0
for c in range(1, num + 1):
    if num % c == 0:
        q += 1
        print('\033[32m {}\033[m'.format(c), end='')
    else:
        print('\033[31m {}\033[m'.format(c), end='')

print('\nO número {} foi divisível {} vezes.'.format(num, q))
if q == 2:
    print('E, por isso, ele É PRIMO')
else:
    print('E, por isso, ele NÃO É PRIMO')
