n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n), end=' = ')
for c in range(n, 0, -1):
    if c == 1:
        c = c - 1
    if c == 0:
        c = 1
    f = f * c
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    elif c == 1:
        print(' = ', end='')
print('{}'.format(f), end='')
