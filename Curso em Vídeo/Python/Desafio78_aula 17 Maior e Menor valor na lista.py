print('='*12, 'Desafio 78', '='*12)
print()
listanum = []
mai = 0
men = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('\033[1;30m=-\033[m'*17)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O maior valor digitado foi {men}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
print('\033[1;30m-------- Fim do Programa --------\033[m')



