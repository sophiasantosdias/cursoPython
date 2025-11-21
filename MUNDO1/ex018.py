# Seno, Cosseno e Tangente
import math
print('====== DESAFIO 18 ======')
ang = float(input('Digite um ângulo: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O ângulo {} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang, sen, cos, tg))
