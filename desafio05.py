numero = int(input('Digite um número: '))
sucessor = numero + 1
antecessor = numero - 1

print('O sucessor do número {} é {} e o seu antecessor é {}'.format(numero, sucessor, antecessor))

#Segunda forma de fazer a mesma coisa sem as variáveis
print('Analsando o valor {}, seu antecessor é {} e o sucessor é {}'.format (numero, (numero-1), (numero+1)))
