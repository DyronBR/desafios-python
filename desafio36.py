print('{}{}{}'.format('\033[32m', '-=-'*27, '\033[m'))
print('\033[31m              Bem vindo ao programa de simulação de empréstimo!\033[m')
print('{}{}{}'.format('\033[32m', '-=-' * 27, '\033[m'), '\n')

vc = float(input('Digite o valor da casa a ser financiada: \033[32mR$\033[m'))
sa = float(input('Digite o valor do salário atual do cliente: \033[32mR$\033[m'))
an = int(input('Digite em quantos anos o cliente pretende pagar o valor emprestado: '))

pr = vc / (an * 12)

if pr > sa * (30 / 100):
    print('\n\033[32mA parcela total desse empréstimo ficaria em R${:.2f}\033[m. \n\033[37mSinto muito, mas sua parcela'
          ' excede o valor máximo permitido.\n\033[35mPara o salário de R${:.2f} o valor máximo é R$ {:.2f}\033[m'
          .format(pr, sa, sa * 30 / 100))
    print('\033[31mEMPRÉSTIMO NEGADO!\033[m')
elif pr <= sa * (30/100):
    print('\n\033[34mParabéns! SEU EMPRÉSTIMO FOI APROVADO!\033[m')
    print('\033[31mVocê deverá pagar o valor de R${:.2f}, durante {:.0f} meses.\033[m'.format(pr, an * 12))
