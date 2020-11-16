print('='*12, 'Desafio 28', '='*12)
print()
from random import randint
from time import sleep

computador = randint(0, 5) # faz o computador pensar
print('-=-'*18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*18)
print()
jogador = int(input('Em que número estou pensando? ')) # jogador tenta adivinhar
print()
print('PROCESSANDO...')
sleep(2)
print()
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {}, e não no número {}!'.format(computador, jogador))