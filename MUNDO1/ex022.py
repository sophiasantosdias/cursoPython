# Analisador de Textos
print('====== DESAFIO 22 ======')

nome = input('Digite seu nome completo: ').strip()
print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
print('O total de caracteres é {}, sem espaços.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(len(nome.split()[0])))
