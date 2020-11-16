print('='*12, 'Desafio 72', '='*12)
print()

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
     'Dez', 'Onze', 'Doze', 'Treze', 'Catorze','Quinze', 'Dezesseis', 'Dezessete',
     'Dezoito', 'Dezenove', 'Vinte')


while True:
    resp = ' '
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print('\033[1;32mVocê digitou o número {} \033[m'.format(cont[num]))
        print()
    else:
        print('\033[1;31mTente Novamnete. Digite um número de 0 a 20! \033[m')
    print()
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print()
print('\033[30m-\033[m'*12,'\033[30mFim do Programa, Volte Sempre!!!','\033[30m-\033[m'*12)





