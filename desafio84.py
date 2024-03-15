temporário = []
nome_e_peso = []
pesoMa = pesoMe = 0
while True:
    temporário.append(str(input('Nome: ')))
    temporário.append(float(input('Peso: ')))
    if len(nome_e_peso) == 0:
        pesoMa = pesoMe = temporário[1]
    else:
        if temporário[1] > pesoMa:
            pesoMa = temporário[1]
        if temporário[1] < pesoMe:
            pesoMe = temporário[1]
    nome_e_peso.append(temporário[:])
    temporário.clear()
    continuar = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Valor incorreto. Deseja continuar?[S/N]: ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('=-' * 30)
print(f'Foram cadastradas {len(nome_e_peso)} pessoas.')
print('=-' * 30)
print(f'O maior peso foi de {pesoMa}Kg. Peso de', end=' ')
for p in nome_e_peso:
    if p[1] == pesoMa:
        (print(f'[{p[0]}]', end=' '))
print('\n'+'=-' * 30)
print(f'O menor peso foi de {pesoMe}Kg. Peso de', end=' ')
for p in nome_e_peso:
    if p[1] == pesoMe:
        (print(f'[{p[0]}]', end=' '))
print('\n'+'=-' * 30)
