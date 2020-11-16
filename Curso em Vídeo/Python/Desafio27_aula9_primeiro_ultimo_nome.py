print('='*12,'Desafio 27', '='*12)
print()

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print()
print('Olá!, {}'.format(n))
print()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
print()
print('É um grande prazer te conhecer!!!')

