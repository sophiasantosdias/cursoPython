# Analisando Triângulos
print('====== DESAFIO 35 ======')
a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if a < b + c and b < a + c and c < b + a:
    print('Esse triângulo é possível')
else:
    print('Esse triângulo não existe')
