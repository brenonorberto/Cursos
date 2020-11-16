print('='*12, 'Desafio 12', '='*12)
print()

preco = float(input('Qual é o preço do produto R$ '))
desc = int(input('Qual o valor do percentual de desconto '))
novo = preco - (preco * desc / 100)

print('O preço do produto é R$ {:.2f}, e com desconto de {}%, o valor passa a ser R$ {:.2f}'.format(preco, desc, novo))