# Vários números com flag
print('====== DESAFIO 66 ======')
s = q = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    q += 1
print('A quantidade de números digitados é igual a {} e a sua soma é igual a {}.'.format(q, s))
