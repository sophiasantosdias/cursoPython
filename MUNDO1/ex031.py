# Custo da Viagem
dist = float(input('Qual é a distância da viagem? '))
print('Você está preste a iniciar uma viagem de {}KM.'.format(dist))
if dist > 200:
    print('E o preço da sua passagem será R${:.2f}.'.format(dist * 0.45))
else:
    print('E o preço da sua passagem será R${:.2f}.'.format(dist * 0.50))
