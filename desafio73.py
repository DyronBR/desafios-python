brasileirao = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Bragantino', 'Fluminense', 'São Paulo', 'Internacional',
               'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'Cruzeiro', 'Cuiabá', 'Santos', 'Bahia', 'Corinthians',
               'Goiás', 'Vasco da Gama', 'América-MG', 'Coritiba')
print('-=-' * 50)
print(f'Os times da série A do brasileirão, em ordem de colocação, são: {brasileirao}')
print('-=-' * 50)
print(f'Os times da série A do brasileirão 2023 em ordem alfabética são: {sorted(brasileirao)}.')
print('-=-' * 50)
print(f'Os 5 primeiros colocados no brasileirão 2023 são: {brasileirao[:5]}.')
print('-=-' * 50)
print(f'Os 4 últimos colocados no brasileirão 2023 são: {brasileirao[-4:]}.')
print('-=-' * 50)
print(f'O flamengo está na {brasileirao.index("Flamengo") + 1}ª posição.')
