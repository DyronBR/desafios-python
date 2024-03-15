frase = input('Digite um frase: ').strip()

fa = frase.lower()

print('1 - A frase possui {} letras "a"'.format(fa.count('a')))
# Outra forma
print('2 - A frase possui {} letras "a"'.format(frase.lower().count('a')))

print('A primeira letra "a" aparece na posição: {}'.format(fa.find('a')+1))

print('A última letra "a" aparece na posição: {}'.format(fa.rfind('a')+1))

