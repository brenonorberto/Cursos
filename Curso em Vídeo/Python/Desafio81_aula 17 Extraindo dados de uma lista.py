print('='*12, 'Desafio 81', '='*12)
print()
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break
print('-='*17)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrecente são {lista}')
if 5 in lista:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi encontrado!')




