# Jogo do Par ou Ímpar
from random import randint
q = 0
while True:
    jogador = int(input('Diga um número: '))
    escolha = input('Par ou Ímpar [P/I]: ').strip().upper()[0]
    computador = randint(0, 10)
    soma = jogador + computador

    if soma % 2 == 0:
        print(f'O jogador escolheu {jogador} e o comutador {computador}. A soma é igual a {soma}, então deu PAR')
        if escolha == 'P':
            vencer = True
        else:
            vencer = False
    elif soma % 2 == 1:
        print(f'O jogador escolheu {jogador} e o comutador {computador}. A soma é igual a {soma}, então deu ÍMPAR')
        if escolha == 'I':
            vencer = True
        else:
            vencer = False

    if vencer == True:
        print('Você ganhou! Jogue novamente.')
        q += 1
    else:
        break

print('GAME OVER')
print(f'Você venceu {q} vezes')
