# Maior e Menor Peso
print('====== DESAFIO 55 ======')
todos = []
for c in range(0, 5):
    peso = float(input('Digite um peso: '))
    todos += [peso]

maior = sorted(todos)[-1]
menor = sorted(todos)[0]
print('O maior peso lido foi {}.'.format(maior))
print('O menor peso lido foi {}.'.format(menor))
