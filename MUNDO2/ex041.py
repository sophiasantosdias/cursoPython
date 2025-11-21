# Classificando Atletas
from datetime import date
print('====== DESAFIO 40 ======')
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade < 9:
    clas = 'MIRIM'
elif 9 <= idade < 14:
    clas = 'INFANTIL'
elif 14 <= idade < 19:
    clas = 'JÚNIOR'
elif 19 <= idade < 25:
    clas = 'SÊNIOR'
else:
    clas = 'MASTER'

print('O atleta tem {} anos'.format(idade))
print('Classificação: {}'.format(clas))
