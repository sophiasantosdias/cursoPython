# Sorteando uma ordem na lista
import random
print('====== DESAFIO 20 ======')

# MINHA RESOLUÇÃO
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = [a1, a2, a3, a4]
escolha1 = random.choice(alunos)
alunos.remove(escolha1)
escolha2 = random.choice(alunos)
alunos.remove(escolha2)
escolha3 = random.choice(alunos)
alunos.remove(escolha3)
escolha4 = random.choice(alunos)
print('A ordem dos alunos é {}, {}, {} e {}'.format(escolha1, escolha2, escolha3, escolha4))

# MANEIRA MAIS FÁCIL
# random.shuffle(lista)
# print(lista)
