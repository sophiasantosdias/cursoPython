# Aluguel de Carros
print('====== DESAFIO 15 ======')
km = float(input('Quantos quilômetros o carro rodou? '))
dias = int(input('Por quantos dias ele foi alugado? '))
print('Considerando a quantidade de {}km e de {} dias, o valor total do aluguel do veículo é {:.2f}.'.format(km, dias, 60*dias + 0.15*km))