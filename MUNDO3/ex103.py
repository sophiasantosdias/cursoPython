# Ficha do Jogador

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    else:
        gols = int(gols)
    print(f'O Jogador {nome} fez {gols} gol(s) no campeonato.')


n = input('Nome do Jogador: ')
g = input('Número de Gols: ')
ficha(n, g)
