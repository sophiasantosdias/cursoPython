# Progressão Aritmética v2.0
print('====== DESAFIO 61 ======')

t = int(input('Termo inicial: '))
r = int(input('Razão da PA: '))
c = 1

print(t, end=' > ')
while c < 10:
    print(t + c * r, end=' > ')
    c += 1
print('FIM')
