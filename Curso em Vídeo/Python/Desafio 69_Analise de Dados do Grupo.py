print('='*12, 'Desafio 69', '='*12)
print()

tot18 = totH = totM20 = 0

while True:
    print('-' * 12)
    print(' CADASTRO ')
    print('-' * 12)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'F' and idade <= 20:
        totM20 += 1
    if sexo == 'M':
        totH += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*30)
print('O total de pessoas com mais de 18 anos é {} '.format(tot18))
print('Ao todo temos {} Homens cadastrados '.format(totH))
print('E temos {} Mulheres com menos de 20 anos '.format(totM20))



