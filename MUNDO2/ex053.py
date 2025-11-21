# Detector de Palíndromos
print('====== DESAFIO 53 ======')
f = input('Digite uma frase: ').strip().upper()
frase = ''.join(f.split())
inv = ''
for letra in range(len(frase) - 1, -1, -1):
    inv += frase[letra]
print('O Inverso de {} é {}'.format(frase, inv))
if inv == frase:
    print('É Palíndromo')
else:
    print('Não é um Palíndromo')

'''
Outro jeito:
inv = frase[::-1]
Não precisaria do FOR
'''
