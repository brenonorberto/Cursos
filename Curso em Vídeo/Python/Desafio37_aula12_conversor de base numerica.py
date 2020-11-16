print('='*12, 'Desafio 37', '='*12)
print()

from time import sleep

num = int(input('Digite um número inteiro: '))
print('''Escolha umas das bases de conversão
[1} Converter em BINÁRIO
[2] Converter em OCTAL
[3] Converter em HEXADECIMAL''')
print()

opção = int(input('Sua opção: '))
print()

print('FAZENDO CONVERSÃO....')
sleep(2)
print()
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print ('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADÉCIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção INVALIDA, tente novamente')
