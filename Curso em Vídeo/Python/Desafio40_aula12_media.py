n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a media do aluno é {:.1f}'.format(n1, n2, media))
if media >= 5 and media < 7:
    print('Aluno está em RECUPERAÇÃO ')
elif media < 5:
    print('Aluno está REPROVADO')
elif media >= 7:
    print('Aluno está APROVADO')