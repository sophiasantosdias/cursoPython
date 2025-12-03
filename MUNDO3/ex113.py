# Validador de Entradas 2.0

def leiaInt(str):
    while True:
        num = input(str)
        try:
            num = int(num)
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar nenhum número\033[m')
            num = 0
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        else: 
            break

    return num


def leiaFloat(str):
    while True:
        num = input(str)
        try:
            num = float(num)
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar nenhum número\033[m')
            num = 0
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        else:
            break
    
    return num

i = leiaInt('Digite um inteiro: ')
r = leiaFloat('Digite um real: ')
print(f'Você acabou de digitar o inteiro {i} e o real {r}')
