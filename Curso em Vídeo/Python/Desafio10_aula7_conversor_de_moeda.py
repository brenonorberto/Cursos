print('='*20, 'Desafio 10', '='*20)
print()
real = float(input('Quanto você tem na carteira? R$ '))
dolar = real / 3.30
euro = real / 4.06

print('Com R$ {}, você compra\nUS$ {:.2f}\nEu$ {:.2f}'.format(real, dolar, euro))