# Separando dígitos de um número
print('====== DESAFIO 23 ======')
num = int(input('Digite um número: '))
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(num % 10))
print('Dezana: {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Milhar: {}'.format(num // 1000 % 10))
