# Alistamento Militar
from datetime import date

print('====== DESAFIO 39 ======')
print('''Escolha de acordo com seu gênero:
[ 1 ] Mulher
[ 2 ] Homem''')
sexo = int(input('Sua Opção: '))

if sexo == 1:
    print('Você não precisa se alistar!')
elif sexo == 2:
    nasc = int(input('Digite o ano do seu nascimento: '))
    atual = date.today().year
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('SE ALISTE IMEDIATAMENTE')
    elif idade < 18:
        print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
    else: # Idade > 18
        print('Você deveria ter se alistado há {} anos.'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(atual - (idade - 18)))
else:
    print('Escolha novamente!')
