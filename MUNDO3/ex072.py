# Número por Extenso
numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um valor entre 0 e 20: '))
while True:
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num-1]}')
        break
    else:
        num = int(input('Você digitou um número inválido. Digite outro entre 0 e 20: '))
    