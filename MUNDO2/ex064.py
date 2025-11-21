# Tratando vários números
print('====== DESAFIO 64 ======')
n = 0
c = -1
s = -999
while n != 999:
    n = int(input('Digite um número [999 PARA PARAR]: '))
    c += 1
    s += n
print('Você parou o programa com {} números e a soma é {}'.format(c, s))
