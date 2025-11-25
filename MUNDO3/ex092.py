# Cadastro de Trabalhador
from datetime import date

trabalhador = {}

trabalhador['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
trabalhador['idade'] = date.today().year - nasc
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = input('Salário: R$')
    trabalhador['aposentadoria'] = trabalhador['contratação'] + 35 - nasc

print('-=' * 30)

for k, v in trabalhador.items():
    print(f' - {k} tem valor {v}')
