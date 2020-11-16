print('='*12, 'Desafio 74', '='*12)
print()

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados são: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print(f'\nO Maior número sorteado foi: {max(numeros)}')
print(f'O Menor valor sorteado foi: {min(numeros)}')


