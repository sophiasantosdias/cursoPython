# Unindo Dicionários e Listas

cadastro = {}
pessoas = []
soma = 0

while True:
    cadastro['nome'] = input('Nome: ')
    
    sexo = input('Sexo: [M/F] ')
    while sexo not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F!')
        sexo = input('Sexo: [M/F] ')
    cadastro['sexo'] = sexo
    
    cadastro['idade'] = int(input('Idade: '))
    
    pessoas.append(cadastro.copy())
    cadastro.clear()

    resp = input('Quer continuar? [S/N] ')
    while resp not in 'SsNn':
        print('ERRO! Digite apenas S ou N!')
        resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')

for i, v in enumerate(pessoas):
    soma += v['idade']
media = soma / len(pessoas)
print(f'B) A média das idades é de {media:.2f} anos')

print('C) As mulheres cadastradas foram: ', end='')
for i, v in enumerate(pessoas):
    if v['sexo'] in 'Ff':
        print(v['nome'], end='... ')

print('\nD) Lista das pessoas que estão acima da média: ')
for i, v in enumerate(pessoas):
    if v['idade'] > media:
        print(f'nome = {v['nome']}; sexo = {v['sexo']}; idade = {v['idade']}')

print('<<< ENCERRADO >>>')
