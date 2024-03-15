from random import randint
from time import sleep
jogo = []
palpites = []
print('-' * 40)
print(f'{"JOGAR NA MEGA SENA":^40}')
print('-' * 40)
quantidade = int(input('Digites quantos jogos serão gerados: '))
print(f'-=-=-=-= SORTEANDO {quantidade} JOGOS -=-=-=-=')
for c in range(0, quantidade):
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        if len(jogo) == 6:
            break
    palpites.append(jogo[:])
    jogo.clear()
for lista in range(0, len(palpites)):
    palpites[lista].sort()
    print(f'Jogo {lista + 1}: {palpites[lista]}')
    sleep(1)
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
