print('=' * 40)
print(f'{"BANCO DYRON":^40}')
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$'))
t50 = t20 = t10 = t1 = 0
valor_restante = valor
while True:
    if valor_restante < 50:
        break
    t50 += 1
    valor_restante -= 50
while True:
    if valor_restante < 20:
        break
    t20 += 1
    valor_restante -= 20
while True:
    if valor_restante < 10:
        break
    t10 += 1
    valor_restante -= 10
while True:
    if valor_restante < 1:
        break
    t1 += 1
    valor_restante -= 1
if t50 > 0:
    print(f'Total de {t50} cédulas de R$50.00')
if t20 > 0:
    print(f'Total de {t20} cédulas de R$20.00')
if t10 > 0:
    print(f'Total de {t10} cédulas de R$10.00')
if t1 > 0:
    print(f'Total de { t1} cédulas de R$1.00')
print('=' * 40)
print('Volte sempre ao BANCO DYRON! Tenha um bom dia!')
