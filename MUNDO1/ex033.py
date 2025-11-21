# Maior e Menor Valor
print('====== DESAFIO 33 ======')
num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo Valor: '))
num3 = int(input('Terceiro Valor: '))

'''if num1 > num2:
    if num1 > num3:
        print('O maior valor digitado é {}.'.format(num1))
        if num2 > num3:
            print('O menor valor digitado é {}.'.format(num3))
        else:
            print('O menor valor digitado é {}.'.format(num2))
    else:
        print('O maior valor digitador é {}.'.format(num3))
        print('O menor valor digitado é {}.'.format(num2))
else:
    if num2 > num1:
        if num2 > num3:
            print('O maior valor digitado é {}.'.format(num2))
            if num1 > num3:
                print('O menor valor digitado é {}.'.format(num3))
            else:
                print('O menor valor digitado é {}.'.format(num1))
        else:
            print('O maior valor digitado é {}.'.format(num3))
            print('O maior valor digitado é {}.'.format(num1))'''

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('O menor valor digitado é {}.'.format(menor))

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O maior valor digitado é {}.'.format(maior))

# Problema desses códigos: quando os números repetem, mas para números diferentes, ambos funcionam