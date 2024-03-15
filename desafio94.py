dados = {}
pessoas = []
soma = media = 0
while True:
    dados['nome'] = (str(input('Nome: ')))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'FfMm':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo [M/F]: '))
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    pessoas.append(dados.copy())
    dados.clear()
    if continuar == 'N':
        break
for lista in range(0, len(pessoas)):
    if pessoas[lista]['idade']:
        soma += pessoas[lista]['idade']
media = soma / len(pessoas)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for lista in range(0, len(pessoas)):
    if pessoas[lista]['sexo'] == 'F':
        print(f'{pessoas[lista]["nome"]}', end=' ')
print('\nD) Lista das pessoas que estão acima da média:')
for lista in range(0, len(pessoas)):
    if pessoas[lista]['idade'] > media:
        print(f'{pessoas[lista]["nome"]} com {pessoas[lista]["idade"]} anos.')
print('<< ENCERRADO >>')
