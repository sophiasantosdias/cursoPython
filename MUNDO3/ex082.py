# Dividindo valores em listas

lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

print(f'A lista completa é {lista}')

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'A lista dos pares é {par}')
print(f'A lista dos ímpares é {impar}')        
