# Extraindo dados de uma lista

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    cont = input('Quer continuar? [S/N] ').upper()
    if 'N' in cont:
        break

print(f'Foram digitados {len(lista)} elementos')
print(f'Aqui está a lista em ordem descrescente {sorted(lista, reverse=True)}')

if 5 in lista:
    print('O valor 5 faz parte da lista')
else: 
    print('O valor 5 não faz parte da lista')