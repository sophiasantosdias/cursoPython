# Função para descobrir o maior valor

def maior(* lst):
    print('-='*20)
    print('Analisando os valores passados...')
    quant = len(lst)
    print(f'{lst}. Foram informados {quant} valores ao todo')

    if quant == 0:
        maior = 'INEXISTENTE'
    else:
        maior = sorted(lst)[-1]
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 11)
maior(4, 7, 0)
maior(1, 2)
maior()
