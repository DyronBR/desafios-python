def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é {a}m².')


# Programa Principal
print('-' * 22)
print(' Controle de Terrenos')
print('-' * 22)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print('-' * 22)
área(l, c)
