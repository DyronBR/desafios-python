lista = [[], []]
print('-=' * 30)
print(f'{"Vamos separar 7 valores em par e impar":^60}')
print('-=' * 30)
for c in range(0, 7):
    valores = int(input(f'Digite o {c + 1}º valor: '))
    if valores % 2 == 0:
        lista[0].append(valores)
    else:
        lista[1].append(valores)
lista[0].sort()
lista[1].sort()
print(f'os valores pares são: {lista[0]}')
print(f'Os valores impares são: {lista[1]}')
