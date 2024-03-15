'''
# Um mondo de encontrar a média de forma bem fácil
listaN = []
listaI = []
listaS = []
for pessoa in range(1, 5):
    nome = input('Digite o nome da {}ª pessoa: '.format(pessoa))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(pessoa)))
    sexo = input('Digite o sexo da {}ª pessoa: '.format(pessoa))
    listaN.append(nome)
    listaI.append(idade)
    listaS.append(sexo)
media = listaI[int] / 4
print('A media de idade do grupo é de {} anos'.format(media))
'''

# Outro jeito de fazer:
homem_mais_velho = 0
idade_mais_velho = 0
mulher_menor_de_20 = 0
soma_de_idade = 0
for pessoa in range(1, 5):
    nome = input('Digite o nome da {}ª pessoa: '.format(pessoa))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(pessoa)))
    sexo = input('Digite o sexo da {}ª pessoa (M/F): '.format(pessoa)).strip()
    soma_de_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        homem_mais_velho = nome
        idade_mais_velho = idade
    else:
        if idade > idade_mais_velho:
            homem_mais_velho = nome
            idade_mais_velho = idade
    if sexo in 'Ff' and idade < 20:
        mulher_menor_de_20 += 1
media = soma_de_idade / 4
print('A media de idade do grupo é {:.2f}.'.format(media))
print('Há {} mulheres com menos de 20 anos.'.format(mulher_menor_de_20))
print('O homem mais velho se chama {} e possui {} anos'.format(homem_mais_velho, idade_mais_velho))
