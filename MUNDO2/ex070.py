# Estatísticas em produtos

soma = caros = q = valorMenor = 0
nomeMenor = ''
print('======= LOJA SUPER BARATÃO =======')
while True:
    nomeDoProduto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))

    q += 1
    soma += preco

    if preco >= 1000:
        caros += 1

    if q == 1 or preco < valorMenor:
        nomeMenor = nomeDoProduto
        valorMenor = preco

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').strip().upper()[0]

    if resp == 'N':
        break

print('====== FIM DO PROGRAMA ======')
print(f'O total da conta foi: R${soma:.2f}')
print(f'O total de produtos que custam mais de R$1000,00: {caros}')
print(f'O nome do produto mais barato é: {nomeMenor}')
