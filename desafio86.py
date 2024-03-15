matriz = [[], [], []]
for m1 in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {m1}]: ')))
for m2 in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1, {m2}]: ')))
for m3 in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2, {m3}]: ')))
print('-=' * 30)
for lista in range(0, 3):
    for posição in range(0, 3):
        print(f'[{matriz[lista][posição]:^5}]', end='')
    print()
