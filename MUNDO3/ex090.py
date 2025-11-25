# Dicionários em Python

aluno = {}

aluno['nome'] = input('Nome: ')
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'EM RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'

print('-=-' * 15)

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
