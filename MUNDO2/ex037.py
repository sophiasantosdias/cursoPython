# Conversor de bases numéricas
import math
print('====== DESAFIO 37 =======')
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão')
print('[ 1 ] Binário')
print('[ 2 ] Octal')
print('[ 3 ] Hexadecimal')
base = int(input('Sua opção: '))

if base == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida')
