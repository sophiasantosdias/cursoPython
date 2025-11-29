# Interactive Helping System

from colorama import init, Back

init()

def title(frase, color):
    print(color, end='')
    print('~'*(len(frase) + 4))
    print('  ' + frase)
    print('~'*(len(frase) + 4))


def pyHelp(command):
    print('\033[m')
    help(command)
        

while True:
    title('SISTEMA DE AJUDA pyHELP', color=Back.GREEN)
    print(Back.BLACK, end='')
    p = input('Função ou Biblioteca > ')
    if p.upper() == 'FIM':
        break
    else:
        title(f"ACESSANDO O MANUAL DO COMANDO '{p}'", color=Back.BLUE)
        pyHelp(p)
    