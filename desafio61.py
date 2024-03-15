print('Gerador de P.A.')
print('-=-' * 10)
pt = int(input('Digite o primeiro termo: '))
print('-=-' * 10)
r = int(input('Digite a razão da P.A.: '))
print('-=-' * 10)
termo = pt
contador = 1
while contador <= 10:
    print('{}'.format(termo), end=' → ')
    contador = contador + 1
    termo = termo + r
print('Acabou!')
