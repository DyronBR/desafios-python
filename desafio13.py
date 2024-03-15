nome = input('Digite o nome do funcionário? ')
salario = float(input('Qual o salário atual do funcionário? R$ '))
novo = salario + (salario * 15/100)

print('O novo salário com o aumento de 15% de {} será de R$ {:.2f}.'.format(nome, novo))
