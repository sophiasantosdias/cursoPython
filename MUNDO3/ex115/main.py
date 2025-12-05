# Menu em Pyhton
from lib import interface
try:
    open('MUNDO3/ex115/pessoas.txt', 'a')
except:
    print('\033[31mErro ao tentar abrir o arquivo\033[m')
else:
    print('Arquivo lido/criado com sucesso!')

interface.mainMenu()
