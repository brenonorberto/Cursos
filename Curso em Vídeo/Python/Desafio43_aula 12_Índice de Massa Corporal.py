print('=' * 12, 'Desafio 43', '=' * 12)
print()

peso = float(input('Digite o seu peso (KG)! '))
altura = float(input('Digite a sua altura (M)! '))
imc = peso / (altura ** 2)
print()
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO NORMAL!')
elif 18.5 <= imc < 25:  # também pode ser feito dessa forma ( imc >= 18.5 and imc < 25 )
    print('PARABÉNS!, Você está na faixa de PESO NORMAL! ')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('CUIDADO!, Você está em OBSIDADE MÓBIDA')
