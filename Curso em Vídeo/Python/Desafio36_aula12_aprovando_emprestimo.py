print('\033[33m=\033[m'*12, '\033[30mDesafio 36\033[m', '\033[33m=\033[m'*12)
print()

from time import sleep

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Qual a quantidade de parcelas? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print()
print('\033[1;33mFANZENDO OS CALCULOS...\033[m')
sleep(2)

print()
print('Para pagar uma casa de \033[1;30mR${:.2f}\033[m, em \033[1;30m{} Anos\033[m, a prestação será de \033[1;30m{:.2f}\033[m'.format(casa, anos, prestação))
if prestação <= minimo:
    print('\033[1;32mEmprestimo CONCEDIDO!\033[m')
else:
    print('\033[1;31mEmprestimo NEGADO!\033[m')
