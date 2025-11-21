# Analisador Completo
print('====== DESAFIO 56 ======')
nomes = []
somaIdades = 0
maior = 0
nomeMaior = ''
q = 0

for p in range(0, 4):
    print('----- {}ª PESSOA -----'.format(p + 1))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').upper()

    nomes += [nome]
    somaIdades += idade

    if sexo == 'M':
        if p == 0:
            maior = idade
            nomeMaior = nomes[0]
        else:
            if maior < idade:
                maior = idade
                nomeMaior = nomes[p]
    elif sexo == 'F':
        if idade < 20:
            q += 1
    else:
        print('Escolha se sexo inválida')


m = somaIdades / 4
print('A média de idade do grupo é {} anos'.format(m))
print('O homem mais velho é {}'.format(nomeMaior))
print('A quantidade de mulheres que tem menos de 20 anos é {}'.format(q))
