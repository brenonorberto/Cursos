print('='*12, 'Desafio 12', '='*12)
print()

from datetime import date

atual = date.today().year
data = int(input('Digite o ANO do seu nascimento: '))
idade = atual - data
print('O atleta tem {} Anos'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
