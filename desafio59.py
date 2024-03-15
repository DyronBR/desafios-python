from time import sleep

print('-=-' * 12+'\n'+'PROGRAMA DE CALCULOS MATEMÁTICOS'+'\n'+'-=-' * 12)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('PROCESSANDO...')
sleep(1)
op = 0
while op != 5:
    print('''
    ------------------------
    \033[31m[1]\033[m Somar
    \033[31m[2]\033[m Multiplicar
    \033[31m[3]\033[m Maior
    \033[31m[4]\033[m Novos números
    \033[31m[5]\033[m Sair do programa
    ------------------------
    ''')
    op = int(input('Digite a opção desejada: '))
    print()
    if op == 1:
        print('{:.2f} + {:.2f} = {:.2f}\n'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('{:.2f} x {:.2f} = {:.2f}\n'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('{:.2f} é maior que {:.2f}\n'.format(n1, n2))
        elif n2 > n1:
            print('{:.2f} é maior que {:.2f}\n'.format(n2, n1))
        else:
            print('{:.2f} é igual a {:.2f}\n'.format(n1, n2))
    elif op == 4:
        print('Tudo bem. Vamos recomeçar.\n')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif op == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente.\n')
        print('PROCESSANDO...')
        sleep(1)
print('Programa encerrado! Volte sempre!')
