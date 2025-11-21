# Simulador de Caixa Eletrônico

quant50 = quant20 = quant1 = 0
print('======= BANCO DA SOPHIA =======')
valor = float(input('Qual valor você deseja sacar? R$'))

while (valor - 50) >= 0:
    quant50 += 1
    valor -= 50

while (valor - 20) >= 0:
    quant20 += 1
    valor -= 20

while (valor - 1) >= 0:
    quant1 += 1
    valor -= 1

if quant50 > 0:
    print(f'Total de {quant50} cédulas de R$50,00')
if quant20 > 0:
    print(f'Total de {quant20} cédulas de R$20,00')
if quant1 > 0:
    print(f'Total de {quant1} cédulas de R$1,00')
