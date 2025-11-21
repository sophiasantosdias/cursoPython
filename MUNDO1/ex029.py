# Radar Eletrônico
vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format((vel - 80) * 7))
print('Tenha um bom dia e dirija com segurança.')
