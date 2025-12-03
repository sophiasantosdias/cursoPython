# Site acessível?
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('\033[31mO Site Pudim não está acessível no momento\033[m')
else:
    print('O Sitem Pudim está acessível no momento')
