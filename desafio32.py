from calendar import isleap
from datetime import date

ano = int(input('Digite um ano qualquer. Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))

# Outro modo de calcular se o ano é bissexto, onde se lê, O ano dividido por 4, tem resto 0 e
# o ano dividido por 100 não pode ser diferente de zero ou o ano ser dividido por 400 com resto 0

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('2 - O ano {} é bissexto!'.format(ano))
else:
    print('2 - O ano {} não é bissexto!'.format(ano))
