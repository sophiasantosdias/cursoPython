# Análise de dados do grupo

maiordeidade = 0
quantHomem = 0
mulhermenorde20 = 0

while True:
    print('-------------------')
    print('CADASTRE UMA PESSOA')
    print('-------------------')

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper().strip()[0]
    print('-------------------')

    if idade >= 18:
        maiordeidade += 1

    if sexo == 'M':
        quantHomem += 1

    if sexo == 'F' and idade < 20:
        mulhermenorde20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]

    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maiordeidade}')
print(f'Total de homens cadastrados: {quantHomem}')
print(f'Total de mulheres com menos de 20 anos: {mulhermenorde20}')

