print('Gerador de P.A.')
print('-=-' * 10)
pt = int(input('Digite o primeiro termo: '))
print('-=-' * 10)
r = int(input('Digite a razão da P.A.: '))
print('-=-' * 10)
termo = pt
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{}'.format(termo), end=' → ')
        contador = contador + 1
        termo = termo + r
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('Progressão finalizada com {} termos mostrados.'.format(total))
