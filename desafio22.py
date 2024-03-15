# Terminar com .strip, faz com que elimine os espaços do começo e do final da variável
nome = input('Digite o seu nome completo: ').strip()

# Mostrar o nome com todas as letras maiúsculas
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
# Mostrar o nome com todas as letras minúsculas
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
# Mostrar quantas letras ao todo tem o nome sem considerar os espaços
espaço = nome.replace(' ', '')
print('1 - Seu nome tem ao todo {} letras.'.format(len(espaço)))
# Mostrar quantas letras ao todo removendo os espaços
print('2 - Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
# Mostrar quantas letras tem o primeiro nome
pm = nome.split()
print('Seu primeiro nome é {}'.format(pm[0]))
print('1 - Seu primeiro nome tem {} letras.'.format(len(pm[0])))
# Mostrar quantas letras tem o primeiro nome, de outro modo é usar o comando find, para achar o primeiro espaço
print('2 - Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
