# Valores únicos em uma lista

lista = []

while True:
    val = int(input('Digite um valor: '))
    if val not in lista:
        lista.append(val)
        print('Valor adicionado com sucesso...')
    else:
        print('Esse valor já está na lista. Não vou adicioná-lo')

    cont = input('Deseja continuar? [S/N] ')[0]
    if cont in 'Nn':
        break
print('Programa Encerrado!')
print(f'Você digitou os valores {sorted(lista)}')
