nome = input('Digite o nome do aluno? ')
nt1 = float(input('Digite a primeira nota do aluno: '))
nt2 = float(input('Digite a segunda nota do aluno: '))
media = (nt1 + nt2) / 2

print('A média do aluno {} é {:.1f}.'.format(nome, media))
