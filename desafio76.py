listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
material1 = 0
valor1 = 0
while True:
    material1 += 2
    valor1 += 2
    if material1 > len(listagem):
        break
    if material1 == 2:
        material = listagem[material1 - 2]
        valor = listagem[valor1 - 1]
    else:
        material = listagem[material1 - 2]
        valor = listagem[valor1 - 1]
    print(f'{material:.<30}R${valor:>7.2f}')
print('-' * 40)
print()

# Outro modo
print('-' * 40)
for posicao in range(0,len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:>7.2f}')
print('-' * 40)
