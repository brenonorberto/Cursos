print('='*12, 'Desafio 52', '='*12)
print()

num = int(input('Digite um número: '))
print()
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;33m', end='')
        tot += 1
    else:
        print('\033[30m', end='')

    print('{} '.format(c), end='')
print('\n\033[mO número {}, foi divisivel {} vezes'.format(num, tot))
if tot % 2:
    print('E por isso ele é um número PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

