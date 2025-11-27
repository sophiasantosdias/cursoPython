# Validador de Entradas

def leiaInt(str):
    while True:
        num = input(str)
        if num.isnumeric():
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
    return (int(num))


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
