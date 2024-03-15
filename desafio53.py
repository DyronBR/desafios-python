frase = str(input('Digite uma frase: ')).lower().strip(' ')

print('Você digitou a frase: {}'.format(frase))

frasesemespaço = frase.replace(' ', '')

inverso = frasesemespaço[::-1]

if frasesemespaço == frasesemespaço[::-1]:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
print(frasesemespaço)

print()
print()

# outro modo de fazer a mesma coisa

frase2 = str(input('Digite uma frase: ')).lower().strip(' ')
palavras = frase2.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
