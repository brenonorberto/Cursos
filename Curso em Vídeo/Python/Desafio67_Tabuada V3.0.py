print('='*12, 'Desafio 67', '='*12)
print()

while True:
    n = int(input('Quer ver a Tabuada de que valor?\n(Digite (-99), para encerrar o programa): '))
    print('-'*13)
    if n == -99:
        break
    for c in range(1,11):
        print('{} x {} = {}'.format(n,c,n*c))
    print('-'*13)
print()
print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE!')
