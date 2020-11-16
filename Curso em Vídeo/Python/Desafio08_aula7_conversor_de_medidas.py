print('='*20, 'Desafio 08', '='*20)

medida = float(input('Digite uma media em metros '))
print()
print('{} metro, equivale a\n {:.0f} centimetros \n {:.0f} milimetros \n {} Kilometros '.format(medida, medida * 100, medida * 1000, medida / 1000))