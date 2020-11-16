print('\033[33m=\033[m'*12, '\033[30mDesafio 33\033[m', '\033[33m=\033[m'*12)
print()
from time import sleep
a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))
print()

# Verificando menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('\033[1;32mVerificando números...\033[m')
sleep(2)
print()

print('O Menor número digitado foi \033[1;34m{}\033[m'.format(menor))
print('O Maior número digitado foi \033[1;36m{}\033[m'.format(maior))
sleep(1)
print()
print('\033[1;32m[Programa Finalizado]\033[m')
