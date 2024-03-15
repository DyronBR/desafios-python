from random import randint
from time import sleep
computador = randint(0, 10)
print(computador)
print('-=-' * 17)
print('Vou pensar em um número de 0 a 10. Tente adivinhar: ')
print('-=-' * 17, '\n')
total = 0
acertou = False
while not acertou:
    num = int(input('Qual é o seu palpite: '))
    print('PROCESSANDO...')
    sleep(1)
    total += 1
    if num == computador:
        acertou = True
    else:
        if num < computador:
            print('Mais... Tente mais uma vez.')
        elif num > computador:
            print('Menos... Tente mais uma vez.')
if total == 1:
    print('Parabéns. Você acertou de primeira. Eu pensei no número {}!'.format(num))
elif total <= 3:
    print('Muito bem! Você acertou e levou apenas {} tentativas. Eu pensei no número {}.'.format(total, computador))
else:
    print('Você acertou. Eu pensei no número {}, mas levou {} tentativas. Dá pra melhorar!'.format(computador, total))
