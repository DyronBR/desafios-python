print('\033[31m' + '-=-' * 20 + '\033[m')
print('         \033[34mPrograma de cálculo de média do aluno!\033[m')
print('\033[31m' + '-=-' * 20 + '\033[m\n')

aluno = input('Digite o nome do aluno: ')
n1 = float(input('Digite o valor da primeira nota do aluno: '))
n2 = float(input('Digite o valor da segunda nota do aluno: '))
media = (n1 + n2) / 2


if media < 5.0:
    print('O aluno {} teve média {}. Sendo assim ele foi \033[31mREPROVADO!\033[m'.format(aluno, media))
elif 5.0 <= media < 7.0:
    print('O aluno {} teve média {}. Sendo assim ele está de \033[33mRECUPERAÇÃO!\033[m'.format(aluno, media))
elif media >= 7.0:
    print('O aluno {} teve média {}. Sendo assim, ele está \033[34mAPROVADO!\033[m'.format(aluno, media))

