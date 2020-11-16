print('\033[33m=\033[m'*12, '\033[30mDesafio 32\033[m', '\033[33m=\033[m'*12)
print()
from datetime import date
from time import sleep
ano = int(input('Que ano você quer analisar? Coloque 0, para o ano atual: '))
print()
print('\033[1;32mPROCESSANDO INFORMAÇÃO...\033[m')
sleep(2)
print()
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1;33m{}\033[m é BISSEXTO'.format(ano))
else:
    print('O ano \033[1;33m{}\033[m NÃO É BISSEXTO'.format(ano))


