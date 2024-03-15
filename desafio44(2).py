print('\033[31m')
print('{:=^60}'.format(' Preço X Condição de pagamento '))
print('\033[m')

preço = float(input('Preço das compras: '))

print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

forma = int(input('\nQual é a opção? '))

if forma == 1:
      total = preço - (preço * 10/100)
      print('Sua compra será paga à vista, em dinheiro ou cheque com desconto.\n'
            'Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif forma == 2:
      total = preço - (preço * 5/100)
      print('Sua compra será paga à vista, no cartão, com desconto.\n'
            'Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif forma == 3:
      print('Sua compra será paga em 2x de R${:.2f} sem juros.\n'
            'Sua compra ficará no valor de R${:.2f} no final.'.format(preço / 2, preço))
elif forma == 4:
      parcelas = int(input('Quantas parcelas? '))
      total = preço + (preço * 20/100)
      print('Sua compra será parcelada em {}x de R${:.2f} com juros.\n'
            'Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(parcelas, total / parcelas, preço, total))
else:
      print('\033[31mVocê digitou uma opção inválida de pagamento\033[m.')
