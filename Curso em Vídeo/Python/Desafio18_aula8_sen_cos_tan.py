print('='*12, 'Desafio 18', '='*12)
print()

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print()

print('O ângulo de {:.0f}° tem: \n\nSENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}'.format(angulo, sen, cos, tan))

