from datetime import date
ano_atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = ano_atual - nascimento
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print('{} pessoas atingiram a maioridade e {} pessoas ainda não.'.format(total_maior, total_menor))
