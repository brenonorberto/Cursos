print('='*12, 'Desafio 39', '='*12)
print()

from datetime import date

atual = date.today().year
nasc = int(input('Digite o seu ANO de nascimento: '))
idade = atual - nasc
print()

print('Quem nasceu em {}, tem {} anos em {}'.format(nasc, idade, atual ))
if idade == 18:
    print('Esse ano você deve se ALISTAR')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para o ALISTAMENTO'.format(saldo))
    print('Seu alistamento seré em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você deveria ter se alistado a {} anos'.format(saldo))
    print('Se alistamento foi em {}'.format(ano))




