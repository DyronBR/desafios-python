matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaP = soma3c = maior = 0
for lista in range(0, 3):
    for posição in range(0, 3):
        matriz[lista][posição] = int(input(f'Digite o valor [{lista}, {posição}]: '))
print('=-' * 30)
for lista in range(0, 3):
    for posição in range(0, 3):
        print(f'[{matriz[lista][posição]:^5}]', end='')
        if matriz[lista][posição] % 2 == 0:
            somaP += matriz[lista][posição]
        if posição == 2:
            soma3c += matriz[lista][posição]
        if lista == 1:
            if posição == 0:
                maior = matriz[lista][posição]
            if posição > 0:
                if maior < matriz[lista][posição]:
                    maior = matriz[lista][posição]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {somaP}.')
print(f'A soma dos valores da terceira coluna é {soma3c}.')
print(f'O maior valor da segunda linha é {maior}.')
print('=-' * 30)
