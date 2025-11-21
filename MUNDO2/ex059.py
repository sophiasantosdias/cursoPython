# Menu de Opções
print('====== DESAFIO 59 ======')

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
escolha = 0

while escolha != 5:
    print(('''    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior valor 
    [ 4 ] novos números
    [ 5 ] sair do programa'''))
    escolha = int(input('>>>>>> Qual a sua opção? '))
    if escolha == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('O produto entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('O primeiro valor é maior que o segundo.')
        elif n1 < n2:
            print('O segundo valor é maior que o primeiro.')
        else:
            print('Os valores são iguais')
    elif escolha == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha > 5:
        print('Opção Inválida, tente novamente.')
    print('=-=' * 10)
print('FIM!')
