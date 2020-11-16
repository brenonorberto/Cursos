print('='*12, 'Desafio 50', '='*12)
print()

soma = 0
cont = 0
for c in range(1, 7):
    num = (int(input('Digite um {} valor: '.format(c))))
    if num % 2 == 0:
        soma += num
        cont += 1
print()
print('Você digitou {} numeros e a soma dos número PARES é {}'.format(cont, soma))
