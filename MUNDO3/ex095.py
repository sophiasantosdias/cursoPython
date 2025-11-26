# Aprimorando o Ex093

jogadores = []
cadastro = {}
soma = gol = 0
gols = []

while True:
    cadastro['nome'] = input('Nome do Jogador: ')
    quant = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
    for c in range(1, quant + 1):
        gol = int(input(f'  Quantos gols na partida {c}? '))
        gols.append(gol)
        soma += gol
    cadastro['gols'] = gols[:]
    cadastro['soma'] = soma
    gols.clear()
    soma = 0
    jogadores.append(cadastro.copy())
    cadastro.clear()

    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
    
    print('-='*20)

print(f'{'cod':<4}{'nome':<15}{'gols':<15}{'total':>6}')
print('-'*40)
for i, v in enumerate(jogadores):
    print(f'{i:<4}{v['nome']:<15}{str(v['gols']):<15}{v['soma']:<6}')
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if busca == 999:
        print('ENCERRANDO...')
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR: {jogadores[busca]['nome']}')
        for i, v in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i+1} fez {v} gols')

print('<<< VOLTE SEMPRE >>>')
