# Tabuada v3.0
print('====== DESAFIO 67 ======')

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 25)
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
    print('-' * 25)
print('PROGRAMA TABUADA ENCERRADO COM SUCESSO')
