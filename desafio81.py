lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    while r not in 'SsNn':
        r = str(input('Valor incorreto. Deseja continuar?[S/N]: '))
    if r in 'Nn':
        break
print(f'Foi digitado {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A lista de valores digitados, em ordem decrescente é: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
