print('='*12, 'Desafio 17', '='*12)
from math import hypot
print()
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print()
print('A hipotenusa vai medir {:.2f}'.format(hi))