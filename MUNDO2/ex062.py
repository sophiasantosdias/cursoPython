# Super Progressão Aritmética v3.0
print('====== DESAFIO 62 ======')

primeiro = int(input('Termo inicial: '))
r = int(input('Razão da PA: '))
t = primeiro
q = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while q <= total:
        print(t, end=' > ')
        t += r
        q += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer mostrar? '))
print('FIM')
print('A progressão terminou após mostrar {} termos'.format(total))
