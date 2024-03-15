salario = float(input('Digite o salário do funcionário: '))
print('O salário atual do funcionário é R${:.2f}.'.format(salario))
if salario > 1250:
    print('O valor que o funcionário receberá de aumento sera de R${:.2f}. O novo valor será de R${:.2f}'
          .format(salario * (10/100), salario + (salario*(10/100))))
else:
    print('O valor que o funcionário receberá de aumento será de R${:.2f}. O novo valor será de R${:.2f}'
          .format(salario * (15/100), salario + (salario * (15/100))))
