# Soma dos Pares
print('====== DESAFIO 50 ======')
s = 0
q = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        s += n
        q += 1
print('Você informou {} números pares e a soma é {}'.format(q, s))
