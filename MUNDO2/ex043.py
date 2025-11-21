# IMC
print('====== DESAFIO 43 ======')
peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt * alt)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está no peso IDEAL')
elif 25 <= imc < 30:
    print('Cuidado, você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
