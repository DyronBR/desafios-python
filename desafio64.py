print('PARA PARAR DIGITE 999')
num = soma = quantidade = 0
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        soma += num
        quantidade += 1
print('A soma dos {} números digitados é {}.'.format(quantidade, soma))
