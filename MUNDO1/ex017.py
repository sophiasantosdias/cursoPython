# Catetos e Hipotenusas
import math
print('====== DESAFIO 17 ======')
catad = int(input('Digite o cateto adjacente: '))
catop = int(input('Digite o cateto oposto: '))
hip = math.hypot(catad, catop)
print('Se os catetos são {} e {}, a hipotenusa é {}'.format(catad, catop, hip))
