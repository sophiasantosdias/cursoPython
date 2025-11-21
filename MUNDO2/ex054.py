# Grupo da Maioridade
print('====== DESAFIO 54 ======')
from datetime import date
menor = 0
maior = 0
atual = date.today().year
for p in range(1, 8):
    ano = int(input('A {}ª pessoa nasceu em: '.format(p)))
    if (atual - ano) >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
