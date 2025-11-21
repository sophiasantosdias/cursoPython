# Quantidade de litros de tinta (1l = 2m²)
print('====== DESAFIO 11 ======')
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
a = lar*alt

print('Sua parede tem a dimensão de {}x{} e sua área é {}m².'.format(lar, alt, a))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(a/2))