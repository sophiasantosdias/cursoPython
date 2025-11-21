# Soma dos Múltiplos Múltiplos de 3
print('====== DESAFIO 48 ======')
s = 0
q = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        q += 1
        s += c

print('A soma dos {} números solicitados é igual a {}'.format(q, s))
