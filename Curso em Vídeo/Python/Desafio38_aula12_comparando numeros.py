print('='*12, 'Desafio 38', '='*12)
print()

from time import sleep

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
print()

print('COMPARANDO NUMEROS....')
sleep(2)
print()

if n1 > n2:
    print('O primeiro numero é MAIOR')
elif n2 > n1:
    print('O segundo numero é MAIOR')
else:
    print("Não existe valor MAIOR, os dois numeros são IGUAIS")

