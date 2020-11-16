print('\033[33m=\033[m'*12, '\033[30mDesafio 35\033[m', '\033[33m=\033[m'*12)
print()

from time import sleep

r1 = float(input('Digite o 1º segmento: '))
r2 = float(input('Digite o 2º segmento: '))
r3 = float(input('Digite o 3º segmento: '))
print()

print('\033[1;33mVerificando segmentos...\033[m')
sleep(2)
print()
# Para formar um triangulo o valor maior tem que ser menor que a soma dos outros dois.

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;34mFORMAM UM TRIANGULO\033[m')
else:
    print('Os segmentos \033[1;34mNÃO FORMAM UM TRIANGULO\033[m')