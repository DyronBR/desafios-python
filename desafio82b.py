lista = []
listaP = []
listaI = []
while True:
    lista.append(int(input('Digite um valor: ')))
    con = str(input('Deseja continuar?[S/N]]: ')).strip().upper()[0]
    while con not in 'SsNn':
        con = str(input('Valor incorreto. Deseja continuar?[S/N]]: ')).strip().upper()[0]
    if con in 'Nn':
        break
print(f'Lista completa: {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        listaP.append(v)
    else:
        listaI.append(v)
print(f'Lista dos números pares: {listaP}')
print(f'Lista dos números impares: {listaI}')
