# Função para Fatorial

def fatorial(v, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param v: número cujo o fatorial será calculado
    :param show: (opcional) mostrar ou não o processo do fatorial
    :return: o valor do fatorial de um número de valor v
    """
    from time import sleep
    f = 1
    for c in range(v, 0, -1):
        f *= c

        if show:
            print(c, end='')
            if c == 1:
                print(' = ', end='')
            else:
                print(' X ', end='')
             
    return f

    
print(fatorial(7, True))
help(fatorial)
