# Função que calcula Área

def area(x, y):
    print(f'A área de um terreno {x}m x {y}m é de {x*y}m².')
    print('-'*50)


print('-'*50)
print(f'{'CONTROLE DE TERRENOS':^50}')
print('-'*50)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
