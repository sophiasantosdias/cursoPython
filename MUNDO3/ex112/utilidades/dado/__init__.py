def leiaDinheiro(str):
    valido = False
    while not valido:
        entrada = input(str).replace(',', '.').strip()
        if entrada.isalnum() and not entrada.isnumeric() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" não é um número válido\033[m')
        else:
            valido = True
            return float(entrada)
    