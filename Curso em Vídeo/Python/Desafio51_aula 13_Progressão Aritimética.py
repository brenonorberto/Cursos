print('='*12, 'Desafio 51', '='*12)
print()

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
print()
for c in range(primeiro, decimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('ACABOU')