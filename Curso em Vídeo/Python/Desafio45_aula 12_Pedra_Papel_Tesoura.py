print('=' * 12, 'Desafio 45', '=' * 12)
print()

from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = str(input('Qual seu nome Jogador? '))
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print()
print('-=' * 11)
print('Computador jogou {}'.format((itens[computador])))
print('{} jogou {}'.format(jogador, itens[jogada]))
print('-=' * 11)
if computador == 0:
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('{} GANHOU!!!'.format(jogador))
    elif jogada == 2:
        print('Computador GANHOU!!!')
elif computador == 1:
    if jogada == 0:
        print('Computador Ganhou!!!')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('{} GANHOU!!!'.format(jogador))
elif computador == 2:
    if jogada == 0:
        print('{} GANHOU!!!'.format(jogador))
    elif jogada == 1:
        print('Computador GANHOU!!!')
    elif jogada == 2:
        print('EMPATE')





