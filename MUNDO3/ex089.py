# Boletim com listas compostas

cadastro = []
alunos = []
medias = []

while True:
    cadastro.append(input('Nome: '))
    cadastro.append(int(input('Nota 1: ')))
    cadastro.append(int(input('Nota 2: ')))
    medias.append((cadastro[1] + cadastro[2]) / 2)
    alunos.append(cadastro[:])
    cadastro.clear()

    resp = input('Deseja continuar?[S/N] ')
    if resp in 'Nn':
        break

print('-' * 30)
print(f'{'No.':<3}', f'{'NOME':<15}', f'{'MÉDIA':>5}')

for i, v in enumerate(alunos):
    print(f'{i:<3}', f'{v[0]:<15}', f'{medias[i]:>5}')

print('-' * 30)

while True:
    a = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if a == 999:
        break

    print(f'As notas de {alunos[a][0]} são {alunos[a][1:]}')
    print('-' * 30)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
