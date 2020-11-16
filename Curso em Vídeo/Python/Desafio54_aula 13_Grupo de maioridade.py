print('='*12, 'Desafio 54', '='*12)
print()

from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 7):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print()
print('Ao todo tivemos {} pessoas maiores de idade'.format((totmaior)))
print('E também tivemos {} pessoas menores de idade'.format((totmenor)))

