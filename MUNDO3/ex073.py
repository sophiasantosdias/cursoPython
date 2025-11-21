# Tuplas com Times de Futebol

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Botafogo', 'Fluminense', 'Bahia', 'Bragantino', 'Corinthians', 'São Paulo', 'Atlético Mineiro', 'Grêmio', 'Vasco da Gama', 'Ceará', 'Internacional', 'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'Sport')

print('-=-'*10)
print(f'Lista de Times do Brasileirão: {times}')
print('-=-'*10)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=-'*10)
print(f'Os quatro últimos são: {times[-4:]}')
print('-=-'*10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-'*10)
print(f'O Bragantino está na {times.index('Bragantino') + 1}ª posição')
