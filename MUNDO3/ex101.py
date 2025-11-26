# Voto

def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    print(f'Com {idade} anos, seu voto é ', end='')
    
    if idade < 16:
        return 'PROIBIDO'
    elif 16 <= idade < 18 or idade >= 65:
        return 'FACULTATIVO'
    elif 18 <= idade < 65:
        return 'OBRIGATÓRIO'

print(voto(int(input('Digite seu ano de nascimento: '))))
