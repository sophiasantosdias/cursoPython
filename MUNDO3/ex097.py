# Um Print Especial

def escrever(msg):
    tam = len(msg) + 4
    print('~'* tam)
    print(f'  {str(msg)}  ')
    print('~'* tam)


escrever('Olá, Mundo!')
escrever('Meu nome é Sophia')
escrever(input('Digite uma frase: '))
