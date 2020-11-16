print('='*12, 'Desafio 53', '='*12)
print()

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[:: - 1]
'''inverso = '' # outra forma de fazer
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print()
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')