# Contando vogais em Tupla

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[p]} temos: ', end='')
    for l in palavras[p]:
        if l in 'AEIOU':
            print(l, end=' ')
    
