pt = int(input('Digite o primeiro termo da progressão aritmética (P.A.): '))
r = int(input('Digite a razão da P.A.: '))
n10 = pt + r * (10-1)
print('Os 10 primeiros termos dessa P.A. são: ', end='')
for c in range(pt, n10 + 1, r):
    print('{}'.format(c), end='→ ')
print('Acabou!')