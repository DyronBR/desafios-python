print('\033[31m', '-=-' * 20)
print('                 Analisador de triângulos')
print('-=-' * 20, '\033[m\n')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nAs retas podem formar um triângulo.', end=' ')
    if r1 == r2 == r3:
        print('\033[34mEsse é um triângulo equilátero.\033[m')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('\033[34mEsse é um triângulo isósceles.\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[34mEsse é um triângulo escaleno.\033[m')
else:
    print('As retas não podem formar um triângulo.')
