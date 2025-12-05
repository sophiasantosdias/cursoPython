from lib import dados

def linha():
    print('-'*40)


def texto(txt):
    linha()
    print(f'{txt:^40}')
    linha()


def verify():
    while True:
        num = input('Sua opção > ')
        try:
            num = int(num)
            break
        except:
            print('\033[31mERRO! Digite um número válido!\033[m')
    if num < 1 or num > 3:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        mainMenu()
    else:
        return num


def mainMenu():
    texto('MENU PRINCIPAL')

    print('\033[33m1 - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2 - \033[34mCadastrar nova pessoa\033[m')
    print('\033[33m3 - \033[34mSair do Sistema\033[m') 
    linha()

    opc = verify()
    if opc == 1:
        dados.visualisar()
    elif opc == 2:
        dados.cadastrar()
    elif opc == 3:
        texto('Saindo do sistema... Até Logo!')
