print('='*12, 'Desafio 48', '='*12)
print()

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # pode ser escrito tambḿe cont += 1
        soma = soma + c # pode ser escrito tambḿe soma += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
