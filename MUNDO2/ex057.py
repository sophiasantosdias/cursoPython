# Validação de Dados
print('====== DESAFIO 57 ======')

sexo = input('Digite seu sexo: ').upper().strip()[0]
while sexo not in 'FfMm':
    sexo = input('Dado inválido. Por favor, digite o seu sexo: ').upper().strip()[0]
print('Sexo {} digitado com sucesso'.format(sexo))
