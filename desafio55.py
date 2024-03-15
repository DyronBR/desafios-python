lista = []
for pessoa in range(1, 6):
    peso = float(input('Digite o peso em kg da {}ª pessoa: '.format(pessoa)))
    lista.append(peso)
print('O maior peso lido foi {:.1f}kg e o menor foi {:.1f}kg.'.format(max(lista), min(lista)))

# Outro modo de fazer a mesma coisa

maior = 0
menor = 0
for pessoa in range (1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        # Se a for o primeiro peso colocado, ele será tanto o menor quanto o maior peso.
        maior = peso
        menor = peso
    # se não foi o primeiro peso colocado, ou seja, já for o próximo peso lido
    else:
        # Se o novo peso for maior que o maior peso anterior, a variável maior receberá esse novo peso
        if peso > maior:
            maior = peso
        # Porém, se o novo peso for menor que o menor peso anterior, a variável menor que receberá esse novo peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg.'.format(maior))
print('O menos peso lido foi de {}kg.'.format(menor))
