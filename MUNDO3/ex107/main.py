# Módulos
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Com o aumento de 10%, temos {moeda.aumento(p, 10)}')
print(f'Com a diminuição de 50%, temos {moeda.diminuicao(p, 50)}')
