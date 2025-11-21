# Primeiro e último nome de uma pessoa
print('====== DESAFIO 27 ======')
nome = input('Digite seu nome: ').strip().title()
print('Seu primeiro nome é {}.'.format(nome.split()[0]))
print('Seu último nome é {}.'.format(nome.split()[-1]))
