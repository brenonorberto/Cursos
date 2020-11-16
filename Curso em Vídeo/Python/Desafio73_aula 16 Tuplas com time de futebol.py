print('=' * 12, 'Desafio 73', '=' * 12)
print()
times = ('são paulo', 'internacional', 'flamengo', 'palmeiras', 'grêmio', 'atletico mineiro',
         'cruzeiro', 'corinthians', 'américa-mg', 'fluminense', 'botafogo', 'santos', 'vasco da gama'
         , 'vitória', 'bahia', 'atletico-PR', 'chapecoense', 'sport recife', 'ceará', 'paraná')
print('-=-'*15)
print('Lista dos times do brasileirão:\n{}'.format(times))
print('-=-'*15)
print('Os 5 primeiros times são:\n{}'.format(times[0:5]))
print('-=-'*15)
print('Os 4 ultimos times são:\n{}'.format(times[-4:]))
print('-=-'*15)
print('Times em ordem alfabetica {}'.format(sorted(times)))
print('-=-'*15)
print('O Ceará está na {}ª posição'.format(times.index('ceará') + 1))
print('-=-'*15)


