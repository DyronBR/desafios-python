n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
rq = n ** (1/2)

print('O dobro de {} é {}\nO triplo de {} é {}. \nA raiz quadrada de {} é igual a {:.2f}.\n'
      .format(n, dobro, n, triplo, n, rq))

# Outro modo de fazer sem usar tantas variáveis, usando apenas a variável n.

print('O dobro de {} é {}\nO triplo de {} é {}. \nA raiz quadrada de {} é igual a {:.2f}.\n'
      .format(n, (n*2), n, (n*3), n, (n**(1/2))))

# Outro modo de calcular a raiz quadrada

print('A raiz quadrada de {} é {:.2f}'.format(n, pow(n, (1/2))))
