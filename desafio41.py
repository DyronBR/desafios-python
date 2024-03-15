from datetime import date

aa = date.today().year


print('\033[31m')
print('-=-' * 20)
print('Descubra a categoria do atleta de acordo com a sua idade!')
print('-=-' * 20)
print('\033[m')

nome = input('Digite o nome do atleta: ')
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = aa - ano

print()

if idade <= 9:
    print('{} tem {} anos e pertence à categoria \033[34mMIRIM\033[m.'.format(nome, idade))
elif idade <= 14:
    print('{} tem {} anos e pertence à categoria \033[34mINFANTIL\033[m.'.format(nome, idade))
elif idade <= 19:
    print('{} tem {} anos e pertence à categoria \033[34mJUNIOR\033[m.'.format(nome, idade))
elif idade <= 25:
    print('{} tem {} anos e pertence à categoria \033[34mSÊNIOR\033[m'.format(nome, idade))
else:
    print('{} tem {} anos e pertence a categoria \033[34mMASTER\033[m.'.format(nome, idade))
