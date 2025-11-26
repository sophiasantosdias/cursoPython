# Função de Contador
from time import sleep

def contador(i, f, p):
    if p < 0:
        p = -p
    elif p == 0:
        p = 1

    print(f'-'*40)
    print(f'Contagem do {i} ao {f} de {p} em {p}: ')
   
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            cont += p
            sleep(0.5)
        print()
    elif i > f:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            cont -= p
            sleep(0.5)
        print()


contador(1, 10, 1)
contador(10, 0, 2)

print(f'-'*40)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

print(f'-'*40)
