# Módulos
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Com o aumento de 10%, temos {moeda.moeda(moeda.aumento(p, 10))}')
print(f'Com a diminuição de 50%, temos {moeda.moeda(moeda.diminuicao(p, 50))}')
