contador = total_gasto = mais1000 = menor_preço = 0
mais_barato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: R$'))
    contador += 1
    total_gasto += preço
    if preço > 1000.0:
        mais1000 += 1
    if contador == 1 or preço < menor_preço:
        menor_preço = preço
        mais_barato = produto
    continuar = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Valor incorreto. Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total gasto nessa compra: R${total_gasto:.2f}.'
      f'\nQuantidade de produtos com valor maior que R$1000.00: {mais1000}'
      f'\nProduto mais barato: {mais_barato} no valor de R${menor_preço:.2f}')
