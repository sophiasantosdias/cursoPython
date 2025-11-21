# Análise de Dados em uma Tupla

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

nums = (a, b, c, d)

print(f'Você digitou os valores: {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')

if 3 in nums:
    print(f'O valor 3 aparece primeiro na {nums.index(3) + 1}ª posição')
else:
    print('O valor 3 não aparece')

print(f'Os valores pares digitados são: ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ') 
