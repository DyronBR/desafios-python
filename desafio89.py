dados_alunos = []
media = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados_alunos.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Valor incorreto.Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('-=' * 50)
print(f'{"Nº":<3}', f'{"NOME":<30}', f'{"MÉDIA":>10}')
print('-' * 50)
for c in range(0, len(dados_alunos)):
    print(f'{c:<3}', f'{dados_alunos[c][0]:<30}', f'{dados_alunos[c][2]:>9.1f}')
print('-' * 50)
while True:
    código = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))
    if código == 999:
        print('FINALIZANDO...')
        break
    if código > len(dados_alunos) - 1:
        print('Nenhum aluno cadastrado nesse código.')
        print('FINALIZANDO...')
        break
    print(f'Notas de {dados_alunos[código][0]} são {dados_alunos[código][1]}')
