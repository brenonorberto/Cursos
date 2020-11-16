print('='*12, 'Desafio 42', '='*12)

r1 = float(input('Digite o 1º segmento: '))
r2 = float(input('Digite o 2º segmento: '))
r3 = float(input('Digite o 3º segmento: '))
print()


# Para formar um triangulo o valor maior tem que ser menor que a soma dos outros dois.

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAM UM TRIANGULO ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos NÃO FORMAM UM TRIANGULO')