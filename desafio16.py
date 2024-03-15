# Deixar um intervalo entre três aspas faz com que aquele código seja intendido com um comentário, e pare de funcionar.

'''from math import trunc
n = float(input('Digite um número qualquer: '))
print('A parte inteira do número digitado foi {}'.format(trunc(n)))'''

# Outro modo de fazer o mesmo comando

n = float(input('Digite um número qualquer: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))
