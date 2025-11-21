# Média do aluno v2.0
print('====== DESAFIO 10 ======')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2

if m < 5:
    print('\033[31mVOCÊ ESTÁ REPROVADO!\033[m')
elif 7 > m >= 5:
    print('\033[33mVOCÊ ESTÁ DE RECUPERAÇÃO!\033[m')
else: # m >=7
    print('\033[32mVOCÊ ESTÁ APROVADO!\033[m')
