preco = float(input('Qual o preço do produto? '))

novo = preco - (preco * 5 / 100)

print('O produto que custava R$ {:.2f}, está com 5% de desconto, '
      'e está custando: R$ {:.2f}'.format(preco, novo))
