print('=' * 40)
print(f'{"BANCO DYRON":^40}')
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$'))
valor_total = valor
cédula = 50
total_cédula = 0
while True:
    if valor_total >= cédula:
        valor_total -= cédula
        total_cédula += 1
    else:
        if total_cédula > 0:
            print(f'Total de {total_cédula} cédulas de R${cédula:.2f}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédula = 0
        if valor_total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO DYRON! Tenha um bom dia!')
