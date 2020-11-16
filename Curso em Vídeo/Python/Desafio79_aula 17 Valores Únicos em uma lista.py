print('='*12, 'Desafio 79', '='*12)
print()

numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*17)
numeros.sort()
print(f'Você digitou os números {numeros}')
