def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print('Menor item da lista é:',menor([1,3,5,7,22,33]))
print('Maior item da lista é:',maior([1,3,5,7,22,33]))