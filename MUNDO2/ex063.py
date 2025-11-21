# Sequência de Fibonacci v1.0
print('====== DESAFIO 63 ======')
q = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 3

print(t1, end=' > ')
print(t2, end=' > ')

while c <= q:
    t3 = t1 + t2
    print(t3, end=' > ')
    c += 1
    t1 = t2
    t2 = t3
print('FIM')
