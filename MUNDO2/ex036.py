# Aprovando empréstimos
print('====== DESAFIO 36 ======')
casa = float(input('Valor da Casa: R$'))
anos = int(input('Quantos anos de financiamento: '))
sal = float(input('Salário do comprador: R$'))
parcela = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, parcela))

if parcela > sal * 30 / 100:
    print('\033[31mEmpréstimo NEGADO\033[m')
elif parcela <= sal * 30 / 100:
    print('\033[32mEmpréstimo CONCEDIDO\033[m')
