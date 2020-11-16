print('='*12, 'Desafio 44', '='*12)
print()

print('{:*^40}'.format(' Loja do Breno '))
print()

preço = float(input('Digite o valor da compra R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] À vista DINHEIRO
[ 2 } À vista CARTÂO
[ 3 ] 2x no CARTÂO
[ 4 } 3x ou mais no CARTÂO''')
print()
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(totalparc, parcela))
print()
print('Sua compra foi de R$ {:.2f}, e no final vai custar R$ {:.2f} '.format(preço, total))




