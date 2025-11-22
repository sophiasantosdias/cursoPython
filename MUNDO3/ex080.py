# Lista ordenada

listnum = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > listnum[-1]:
        listnum.append(n)
        print('O valor foi adicionado no final da lista')
    else:
        pos = 0
        while pos < len(listnum):
            if n <= listnum[pos]:
                listnum.insert(pos, n)
                print(f'O valor foi adicionado na {pos+1}ª posição')
                break
            pos += 1

print(f'A lista em ordem ficou: {listnum}')