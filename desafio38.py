print('\033[31mVamos comparar dois números inteiros?\033[m\n')

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
print()
if n1 > n2:
    print('\33[32mO primeiro valor é maior!\033[m')
elif n2 > n1:
    print('\033[33mO segundo valor é maior!\033[m')
else:
    print('\033[34mNão existe valor maior, os dois são iguais!\033[m')
