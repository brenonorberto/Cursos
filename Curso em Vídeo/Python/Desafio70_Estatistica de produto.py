print('='*12, 'Desafio 70', '='*12)
print()
tot1000 = cont = 0
while True:
    print('-'*15)
    print(' Loja do Breno ')
    print('-'*15)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    cont += 1
    resp = ' '
    if preco > 1000:
        tot1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print()
print('{:-^40}'. format(' Fim do Programa '))
print('O total da compra foi R$ {:.2f} '.format(preco + preco))
print('Existem {} produtos com preço superior a R$ 1.000,00'.format(tot1000))
print('O produto mair barato foi {} que custa R$ {:.2f}'.format(barato, menor))



