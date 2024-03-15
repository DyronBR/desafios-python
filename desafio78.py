'''
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite a posição {c} da lista: ')))
print('=-' * 30)
print(lista)
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}')
'''

lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('=-' * 30)
print(f'A lista digitada foi: {lista}')
print(f'O menor número digitado foi {menor} na posição ', end='')
for pos, item in enumerate(lista):
    if item == menor:
        print(pos, end='... ')
print(f'\nO maior número digitado foi {maior} na posição ', end='')
for pos, item in enumerate(lista):
    if item == maior:
        print(pos, end='... ')
