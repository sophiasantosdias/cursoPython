# Maior e Menor valores em Lista

lista = []

for p in range(0, 5):
    lista.append(int(input(f'Digite um valor pra posição {p}: ')))
    
print(f'Você digitou os valores {lista}')

maior = max(lista)
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...')

menor = min(lista)
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end=' ')
