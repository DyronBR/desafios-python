valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Deja continuar?[S/N] ')).upper().strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Valor incorreto. Deja continuar?[S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'Os valores únicos digitados, em ordem crescente são: {sorted(valores)}')
