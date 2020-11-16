print('='*12, 'Desafio 59', '='*12)
print()

from time import sleep

n1 = int(input('\033[1mDigite o primeiro número: \033[m'))
n2 = int(input('\033[1mDigite o segundo número: \033[m'))
print()
opção = 0
while opção != 5:
    print('''\033[1;30mO que você quer fazer?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa\033[m''')
    opção = int(input('\033[1;31m>>>> Qual é sua escolha? \033[m'))
    print()
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('O resultado entre {} x {} é {}'.format(n1, n2, multiplicação))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o MAIOR É {}'.format(n1, n2, maior))
    elif opção == 4:
        print('informe os números novamente!')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('\033[1;34mFinalizando programa....\033[m')
    else:
        print('OPÇÃO INVÁLIDA, Tente novamente!')
    print('=-='*10)
    sleep(2)
print('\033[1;32m>>> FIM DO PROGRAMA! VOLTE SEMPRE <<<\033[m')

