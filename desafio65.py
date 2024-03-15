continuar = 'S'
quantidade_de_numeros = soma = maior = menor = 0
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    quantidade_de_numeros += 1
    soma += num
    if quantidade_de_numeros == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()
media = soma / quantidade_de_numeros
print('A media dos {} números digitados é {:.2f}.'.format(quantidade_de_numeros, media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))
