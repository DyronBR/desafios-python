print('\033[31m' + '-=-' * 16 + '\n        Preço X Condição de pagamento\n' + '-=-' * 16 + '\033[m')

pn = float(input('\nDigite o preço do produto: '))
cp = int(input('Digite em quantas vezes será feito o pagamento (1 para Á vista): '))

if cp == 1:
    dc = input('Digite \033[31mD\033[m se o pagamento for em dinheiro ou cheque e \033[31mC\033[m se for em cartão: ')\
        .strip().lower()
    if dc == 'd':
        print('Como você vai pagar à vista, em dinheiro ou chegue, terá um desconto 10%, o que equivale a R${:.2f}.'
              '\nSendo assim seu produto custará \033[31mR${:.2f}\033[m.'.format(pn * (10/100), pn - (pn * (10/100))))
    if dc == 'c':
        print('Como você vai pagar à vista, com cartão, terá um desconto de 5%, o que equivale a R${:.2f}.'
              '\nSendo assim seu produto custará \033[31mR${:.2f}\033[m.'.format(pn * 5/100, pn - (pn * 5/100)))
elif cp == 2:
    print('Pagando em 2x no cartão, seu produto não terá nem desconto nem aumento no valor.'
          '\nSendo assim você ira pagar \033[31mR${:.2f}\033[m nele.'.format(pn))
else:
    print('Você optou por pagar em {} vezes no cartão. Essa modalidade de pagamento possui 20% de juros,'
          '\no que equivale a R${:.2f}. Sendo assim seu produto custará \033[31mR${:.2f}\033[m.'
          .format(cp, pn * 20/100, pn + (pn * 20/100)))

