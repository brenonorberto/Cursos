print('='*12, 'Desafio 23', '='*12)
print()
num = int(input('Informe umm número '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print()
print('Analisando o número....')
print()
print('Unidade é: {}'.format(u))
print('Dezena  é: {}'.format(d))
print('Centena é: {}'.format(c))
print('Milhar  é: {}'.format(m))