from lib import interface
from time import sleep
def pessoa():
    lista = []
    while True:
        try:
            nome = input('Nome (sem acento): ')
        except:
            print('\033[31mErro! Digite um nome válido!\033[m')
        else:
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[31mERRO! Digite uma idade válida!\033[m')
        else:
            break
    lista = [nome, str(idade)]
    return lista

def visualisar():
    interface.texto('PESSOAS CADASTRADAS')
    arq = open('MUNDO3/ex115/pessoas.txt', 'r')
    for linha in arq:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')
    sleep(1)
    interface.mainMenu()
    

def cadastrar():
    interface.texto('NOVO CADASTRO')
    lst = pessoa()
    try:
        arq = open('MUNDO3/ex115/pessoas.txt', 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:    
            arq.write(f'{lst[0]};{lst[1]}\n')
        except:
            print('Erro ao cadastrar!')
        finally:
            print(f'Cadastro de {lst[0]} finalizado com sucesso!')
            lst.clear()
            arq.close()
    sleep(1)
    interface.mainMenu()
