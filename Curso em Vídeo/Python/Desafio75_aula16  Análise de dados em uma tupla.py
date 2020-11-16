print('='*12, 'Desafio 72', '='*12)
print()

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print()
print(f'\033[1;33mVocê digitou os valores {num}\033[m')
print(f'\033[30mVocê digitou o número 9\033[m (\033[1;34m{num.count(9)} vezes\033[m)')
if 3 in num:
    print(f'\033[32mO valor 3 apareceu na {num.index(3)+1}ª posição\033[m')
else:
    print(f'\033[1;31mO valor 3 NÃO FOI INFORMADO!\033[m')
print(f'\033[1;30mOs números pares digitados forma: \033[m', end='')
for p in num:
    if p % 2 == 0:
       print(f'\033[1;30m{p}\033[m', end=' ')
















