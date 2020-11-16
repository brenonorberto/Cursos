print('='*12, 'Desafio 49', '='*12)
print()

num = int(input('Digite um número para ver a tabuada: '))
print()
print('-'*12)

for c in range(1, 11):
    print('|{} x {:2} = {}|'.format(num, c, num * c))

print('-'*12)