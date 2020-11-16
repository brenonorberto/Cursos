print('='*12, 'Desafio 22', '='*12)
print()
nome = str(input('Digite seu nome completo: ')).strip()
print()

print('Analisando seu nome....')
print()

print('Seu nome é {}'.format(nome.title()))
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('A quantidade de letras do seu nome é {}'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {}, e tem {} letras'.format((separa[0]).capitalize(), len(separa[0])))



