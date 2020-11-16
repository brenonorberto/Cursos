print('='*12, 'Desafio 76', '='*12)
print()

listagem = ('Lápis ', 1.75,
            'Borracha ', 2,
            'Caderno ', 15.90,
            'Estojo ', 25,
            'Compasso ', 9.99,
            'Mochila ', 120.32,
            'Caneta ', 1.50,
            'Livro ', 34.90)

print('\033[1m-\033[m'*40)
print(f'\033[1m{"Listagem de Produtos":^40}\033[m')
print('\033[1m-\033[m'*40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f' R${listagem[pos]:>7.2f}')
print('\033[1m-\033[m'*40)





