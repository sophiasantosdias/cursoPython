# Analisando Triângulos v2.0
print('====== DESAFIO 42 ======')
a = int(input('Segmento 1: '))
b = int(input('Segmento 2: '))
c = int(input('Segmento 3: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Esses segmentos formam triângulo EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('Esses segmentos formam triângulo ISÓSCELES')
    else:
        print('Esses segmentos formam triângulo ESCALENO')
else:
    print('Esses segmentos NÃO podem formar triângulos')
