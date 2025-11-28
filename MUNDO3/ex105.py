# Gerando Dicionários

dict = {}

def notas(* lst, sit=False):
    dict['total'] = len(lst)
    dict['maior'] = max(lst)
    dict['menor'] = min(lst)
    dict['média'] = sum(lst) / len(lst)
    
    if sit:
        if dict['média'] >= 7:
            dict['situação'] = 'BOA'
        elif dict['média'] >= 5:
            dict['situação'] = 'RAZOÁVEL'
        else:
            dict['situação'] = 'RUIM'

    return dict

resp = notas(5.5, 2, 10, 4.7, sit=True)
print(resp)
