nome = input('Digite seu nome completo: ').strip()

sep = nome.split()

print('O primeiro nome é: {}\nO último nome é: {}'.format(sep[0], sep[-1]))

# Outra forma
print('O primeiro nome é: {}\nO último nome é: {}'.format(sep[0], sep[len(sep)-1]))
