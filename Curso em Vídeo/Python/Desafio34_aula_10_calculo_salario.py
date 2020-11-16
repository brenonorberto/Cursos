print('\033[33m=\033[m'*12, '\033[30mDesafio 35\033[m', '\033[33m=\033[m'*12)
print()


sal = int(input('Digite seu salário: '))
print()

if sal <= 2000:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)

print('Seu novo salário será: R$ {:.2f}'.format(novo))

