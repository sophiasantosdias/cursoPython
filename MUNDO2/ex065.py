# Maior e menor valor
print('====== DESAFIO 65 ======')
c = s = 0
opcao = 'S'
maior = menor = 0

while opcao == 'S':
    n = int(input('Digite um número: '))
    opcao = input('Você quer continuar? [S/N]: ').strip().upper()
    c += 1
    s += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('A quantidade de números foi {} e a média é {:.1f}'. format(c, s / c))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))

