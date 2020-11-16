print('=' * 12, 'Desafio 15', '=' * 12)
print()

da = int(input('O carro foi alugado por quantos dias? '))
kr = float(input('Quantos KM foram rodados ? '))
print()
pa = da * 60
pk = kr * 0.15
# outra solução seria calcular direto pago (da * 60) + (kr * 0.15)
pg = pa + pk

print('O carro foi alugado por {} dias, rodou {} Km, e o total a ser pago é de R$ {:.2f}'.format(da, kr, pg))
