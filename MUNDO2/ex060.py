# Cálculo de Fatorial
from math import factorial
print('====== DESAFO 60 ======')
num = int(input('Digite um número para calcular seu fatorial: '))
prod = 1

# Método 1
print('O Fatorial de {} é {}'.format(num, factorial(num)))

# Método 2
while num != 1:
    prod *= num
    num += -1
print('O Fatorial de {} é {}'.format(num, prod))
