print('='*12, 'Desafio 19', '='*12)
print()

from random import choice

n1 = str(input('Digite o nome da 1º pessoa: '))
n2 = str(input('Digite o nome da 2° pessoa: '))
n3 = str(input('Digite o nome da 3º pessoa: '))
lista = [n1, n2, n3]
escolhido = choice(lista)
print()

print('A pessoa escolhida foi: {}'.format(escolhido))
