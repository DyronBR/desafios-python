lista = []
listaP = []
listaI = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        listaP.append(num)
    else:
        listaI.append(num)
    con = str(input('Deseja continuar?[S/N]]: ')).strip().upper()[0]
    while con not in 'SsNn':
        con = str(input('Valor incorreto. Deseja continuar?[S/N]]: ')).strip().upper()[0]
    if con in 'Nn':
        break
print(f'Lista completa: {lista}')
print(f'Lista dos números pares: {listaP}')
print(f'Lista dos números impares: {listaI}')
