'''
from math import factorial
num = int(input('Digite um número: '))
ft = factorial(num)
print('O fatorial de {} é {}.'.format(num, ft))
'''


n = int(input('Digite um número para calcular seu fatorial: '))
c = n
# Multiplicação limpa recebe 1, soma recebe 0
f = 1
print('Calculando {}!'.format(n), end=' = ')
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f = f * c
    c = c - 1
print('{}.'.format(f))
