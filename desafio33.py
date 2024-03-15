n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
lista = [n1, n2, n3]
print('O maior número digitado foi o {}.\nO menor número digitado foi o {}.'.format(max(lista), min(lista)))

# outro modo de fazer isso usando if
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n2
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('2 - O menor valor digitado foi {}.'.format(menor))
print('2 - O maior valor digitado foi {}.'.format(maior))
