print('='*12, 'Desafio 77', '='*12)
print()

palavras = ('aprender', 'programa', 'linguagem', 'pythom'
            'curso', 'gratis', 'estudar', 'praticar'
            'fran', 'breno', 'trabalhar', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais', end=' ')
    for v in p:
        if v.lower() in 'aeiou':
            print(f'({v})', end='')
print('\n')

print('-'*18, 'Fim do Programa', '-'*18)

