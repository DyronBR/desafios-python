v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
v4 = int(input('Digite o quarto valor: '))
tupla = (v1, v2, v3, v4)
print(f'Você digitou os valores {tupla}')
if 9 in tupla:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
else:
    print(f'O valor 9 apareceu 0 vezes.')
if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na {tupla.index(3)}ª posição')
else:
    print('O 3 não foi digitado em nenhuma posição.')
if v1 % 2 == 0 or v2 % 2 == 0 or v3 % 2 == 0 or v4 % 2 == 0:
    print('O valores pares são: ', end='')
else:
    print('Não há valores pares digitados')
for par in tupla:
    if par % 2 == 0:
        print(f'{par}', end=' ')
print('\n')

# Outro modo de fazer isso:
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.index(3) + 1}ª posição')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print('Os Valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
