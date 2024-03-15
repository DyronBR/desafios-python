s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} número(s) par(s). A soma desse(s) número(s) é {}.'.format(cont, s))
