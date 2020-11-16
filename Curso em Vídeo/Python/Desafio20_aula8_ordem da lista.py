print('='*12, 'Desafio 20', '='*12)
print()

from random import shuffle

n1 = str(input('Digite o nome da 1º pessoa: '))
n2 = str(input('Digite o nome da 2º pessoa: '))
n3 = str(input('Digite o nome da 3º pessoa: '))

lista = [n1, n2, n3]
shuffle(lista)
print()

print('A ordem dos nomes será: \n\n{}'.format(lista))
