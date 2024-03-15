from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = []
print('O valores sorteados foram: ')
for key, valor in jogo.items():
    print(f'O {key} tirou {valor} no dado:')
    sleep(1)
print('-=' * 30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for item, valor in enumerate(ranking):
    print(f'{item + 1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)
