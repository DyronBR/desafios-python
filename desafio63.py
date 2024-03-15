print('-=-' * 15)
print('{:^45}'.format('Sequência de Fibonacci'))
print('-=-' * 15)
num = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print('-=-' * 15)
print('{} → {}'.format(t1, t2), end=' → ')
termos = 3
while termos <= num:
    t3 = t1 + t2
    termos += 1
    print('{}'.format(t3), end=' → ')
    t1 = t2
    t2 = t3
print('FIM')
print('-=-' * 15)
