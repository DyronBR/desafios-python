print('-=-' * 10)
print('\033[31m           TABUADA\033[m')
print('-=-' * 10)
while True:
    n = int(input('---' * 20 + '\nDigite um número (digite um número negativo para parar): '))
    if n < 0:
        break
    for multiplicador in range(1, 11):
        print(f'{n} x {multiplicador:2} = {n * multiplicador}')
print('-=-' * 15)
print('Obrigado por usar nosso programa!')
