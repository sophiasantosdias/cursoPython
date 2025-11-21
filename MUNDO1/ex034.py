# Aumentos Múltiplos
print('====== DESAFIO 34 ======')
sal = float(input('Digite o salário do funcionário: '))
if sal > 1250:
    aum = 10
else:
    aum = 15
print('O salário do funcionário que era {:.2f}, passa a ser {:.2f}.'.format(sal, sal + sal * aum / 100))
