print('='*12, 'Desafio 66', '='*12)
print()

soma  = cont = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print()
print('\033[1;32mA soma dos {} valores foi {}!\033[m'.format(cont, soma))
