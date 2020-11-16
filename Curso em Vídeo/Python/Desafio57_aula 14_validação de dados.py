print('='*12, 'Desafio 57', '='*12)
print()

sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('DADOS INVALIDOS, Por favor, informe seu sexo! ')).strip().upper()[0]
if sexo == 'M':
    sexo1 = 'MASCULINO'
if sexo == 'F':
    sexo1 = 'FEMININO'
print()
print('Sexo {} registrado com sucesso!!! '.format(sexo1))
