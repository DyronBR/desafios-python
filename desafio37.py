print('{}{}{}'.format('\033[35m', '-=-' * 20, '\033[m'))
print('\033[35m              Programa de base de conversão!\033[m')
print('{}{}{}'.format('\033[35m', '-=-' * 20, '\033[m'),'\n')

num = int(input('Digite o número inteiro que será convertido: '))

print('\n\033[31mCÓDIGOS DAS BASES:\n\n\033[m'
      'Para conversão binária:      1\n'
      'Para conversão octal:        2\n'
      'Para conversão hexadecimal:  3\n')

base = int(input('Digite o código da base a ser utilizada: '))

if base == 1:
    print('\nO valor binário de {} é {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('\nO valor octal de {} é {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('\nO valor hexadecimal de {} é {}.'.format(num, hex(num)[2:]))
else:
    print('\nCódigo inválido. Tente novamente.')
