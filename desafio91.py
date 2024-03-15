from random import randint
from time import sleep
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores sorteados:')
for key, valor in jogo.items():
    print(f'{key} tirou {valor} no dado.')
    sleep(1)
print('-=' * 30)
print(' == RANKING DOS JOGADORES ==')
posição = 0
for key in sorted(jogo, key=jogo.get, reverse=True):
    posição += 1
    print(f'  {posição}º lugar: {key} com {jogo[key]}.')
