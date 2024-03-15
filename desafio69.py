idade18 = homem = mulher20 = 0
while True:
    print('---' * 18)
    print(f'{"CADASTRE UMA PESSOA":^56}')
    print('---' * 18)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    while sexo not in 'FfMf':
        sexo = str(input('Valor incorreto. Digite o sexo [F/M]: ')).strip().upper()[0]
    print('---' * 18)
    if idade >= 18:
        idade18 += 1
    if idade < 20 and sexo == 'F':
        mulher20 += 1
    if sexo == 'M':
        homem += 1
    continuar = str(input('Quer continuar cadastrando? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Valor incorreto. Quer continuar cadastrando? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('---' * 18)
print(f'Das pessoas cadastradas:'
      f'\nHá {idade18} pessoas com mais de 18 anos.'
      f'\nHá {homem} homens.'
      f'\nHá {mulher20} mulheres com menos de 20 anos. ')
