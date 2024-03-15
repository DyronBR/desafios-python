n = int(input('Digite um número: '))
print('\nA tabuada de {} é: \n'.format(n))
print('-=-' * 4)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
print('-=-' * 4)
