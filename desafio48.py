print('Os números ímpares que são múltiplos de três (de 1 até 500) são: ', end='')
s = 0
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        soma += c
        cont = cont + 1
        print(c, end=' ')
print('\nA soma entre todos os número ímpares que são múltiplos de três no intervalo de 1 até 500 é {}'.format(s))
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
