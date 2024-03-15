cidade = input('Digite o nome de uma cidade: ').strip()

# Dizer se a cidade digitada começa com a palavra Santo
s = cidade[:5]
print('santo' in s.lower())

# Outra maneira
print(cidade[:5].lower() == 'santo')

