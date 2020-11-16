print('='*12,'Desafio 26', '='*12)
print()

frase = str(input('Digite uma frase: ')).upper().strip()
print()
print('- Na frase a letra A, aparece {} vezes!'.format(frase.count('A')))
print('- A primeira letra A apareceu na posição {}!'.format(frase.find('A')+1))
print('- A ultima letra A apareceu na posição {}!'.format(frase.rfind('A')+1))
