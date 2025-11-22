# Lisca composta e Análise de Dados

pessoas = []
cadastro = []
pesadoNome = []
leveNome = []
pesado = leve = 0

while True:
    cadastro.append(input('Nome: '))
    cadastro.append(float(input('Peso: ')))
    
    if len(pessoas) == 0:
        pesado = leve = cadastro[1]
    else:
        if cadastro[1] > pesado:
            pesado = cadastro[1]
        if cadastro[1] < leve:
            leve = cadastro[1]
    
    pessoas.append(cadastro[:])
    cadastro.clear()
    
    cont = input('Deseja continuar? [S/N]')
    if cont in 'Nn':
        break

for p in pessoas:
    if p[1] == pesado:
        pesadoNome.append(p[0])
    if p[1] == leve:
        leveNome.append(p[0])

print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {pesado}KG e as pessoas foram: {pesadoNome}')
print(f'O menor peso foi {leve} e as pessoas foram: {leveNome}')
