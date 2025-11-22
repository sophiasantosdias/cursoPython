# Validando expressões matemáticas

exp = input('Digite sua expressão: ')

if exp.count('(') == exp.count(')'):
    print('Sua expressão está válida')
else:
    print('Sua expressão está incorreta!')
