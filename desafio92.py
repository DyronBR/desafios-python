from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
dados['idade'] = idade
dados['aposentadoria'] = dados['contratação'] + 35 - date.today().year + idade
print('-=' * 30)
for key, valor in dados.items():
    print(f'  - {key} tem o valor {valor}.')
