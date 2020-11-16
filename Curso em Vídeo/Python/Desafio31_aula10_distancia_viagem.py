print('\033[33m=\033[m'*12, '\033[30mDesafio 31\033[m', '\033[33m=\033[m'*12)
print()
from time import sleep
distacia = int(input('\033[30mQual a distância da sua viagem? \033[m'))
print()
print('\033[1;32mCALCULANDO...\033[m')
sleep(2)
print()
print('\033[30mVocê está prestes a começar uma viagem de \033[31m{}km\033[m.\033[m'.format(distacia))
print()

if distacia <= 200:
    preço = distacia * 0.50
else:
    preço = distacia *0.45
print('\033[30mE o preço de sua passagem será \033[34mR${:.2f}\033[m\033[m'.format(preço))