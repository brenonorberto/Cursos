print('='*12, 'Desafio 13', '='*12)
print()
sal = float(input('Qual o seu salário ? R$ '))
perc = int(input('Qual o valor do percentual de acrescimo do salário ? '))

acre = sal + (sal * perc / 100)
print()
print('O seu salário era R$ {:.2f}, com {}% de aumento, você passa a ganhar o valor de R$ {:.2f}'.format(sal, perc, acre))