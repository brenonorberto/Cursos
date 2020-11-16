print('='*20, 'Desafio 11', '='*20 )
print()

L = float(input('Digite a largura da parede '))
A = float(input('Digite a altura da parede '))
area = L * A
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(L, A, area))
print('Para pintar a parede você irá precisar de {}l de tinta'.format(tinta))