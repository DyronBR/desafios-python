matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lista in range(0, 3):
    for posição in range(0, 3):
        matriz[lista][posição] = int(input(f'Digite um valor para [{lista}, {posição}]: '))
print('-=' * 30)
for lista in range(0, 3):
    for posição in range(0, 3):
        print(f'[{matriz[lista][posição]:^5}]', end='')
    print()
