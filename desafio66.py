q = s = 0
lista = []
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    q += 1
    lista.append(n)
    s += n
print(f'Os números digitados foram {lista}.')
print(f'A quantidade de números digitados foi {q}.')
print(f'A soma dos números digitados é {s}.')
