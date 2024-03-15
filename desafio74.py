from random import randint
quantidade = 0
while True:
    aleatorio = randint(0, 1000)
    quantidade += 1
    if quantidade == 1:
        a1 = aleatorio
    elif quantidade == 2:
        a2 = aleatorio
    elif quantidade == 3:
        a3 = aleatorio
    elif quantidade == 4:
        a4 = aleatorio
    else:
        a5 = aleatorio
    if quantidade == 5:
        break
lista = (a1, a2, a3, a4, a5)
print(f'Os valores sorteados foram: {lista}')
print(f'O menor número da tupla é: {sorted(lista)[0]}')
print(f'O maior número da tupla é: {sorted(lista)[-1]}')
print()

# Segundo modo que consegui fazer
tupla = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
print(f'\nOs valores sorteados foram: {tupla}')
print(f'O menor número da tupla é: {sorted(tupla)[0]}')
print(f'O maior número da tupla é: {sorted(tupla)[-1]}')
print()

# Tercerio modo de fazer
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')