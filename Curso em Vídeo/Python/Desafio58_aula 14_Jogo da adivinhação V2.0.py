print('='*12, 'Desafio 58', '='*12)
print()

from random import randint
computador = randint(0, 10)
print('\033[1;33mOlá! Sou seu computador....\033[m Acabei de pensar em um número entre 0 e 10, ')
print('Será que você consegue adivinhar qual foi? ')
# variaveis
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez! ')
        elif jogador > computador:
            print('Menos... Tentei mais uma vez! ')
print()
print('Acertou com {} tentativas... \033[1;32mParabéns!\033[m '.format(palpite))
