print('\033[33m=\033[m'*12, '\033[30mDesafio 30\033[m', '\033[33m=\033[m'*12)
print()
from time import sleep
numero = int(input('\033[30mDigite um numero qualquer: \033[m'))
print()
print('\033[1;32mPROCESSANDO NÚMERO...\033[m')
sleep(2)
resultado = numero % 2
print()
if resultado == 0:
    print('O número é \033[1;34mPAR\033[m')
else:
    print('O número é \033[1;34mÍmpar\033[m')

print()
sleep(1)
print('-'*5,'\033[1;33mPrograma finalizado\033[m', '-'*5)
