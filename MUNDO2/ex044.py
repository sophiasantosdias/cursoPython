# Gerenciador de Pagamento
print('====== DESAFIO 44 ======')
valor = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no PIX
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = int(input('Qual é a opção? '))

if opc == 1:
    valFin = valor * 90 / 100
elif opc == 2:
    valFin = valor * 95 / 100
elif opc == 3:
    valFin = valor
elif opc == 4:
    valFin = valor * 120 / 100
    parcela = int(input('Quantidade de parcelas: '))
    print('O valor mensal ficará igual a {:.2f}.'.format(valFin / parcela))
else:
    valFin = 0
    print('Opção Inválida')

print('O valor de {:.2f} ficará, no final, igual a {:.2f}'.format(valor, valFin))
