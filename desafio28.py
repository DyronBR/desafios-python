from random import randint
from time import sleep

# Fa o computador "pensar" em um número randômico entre 0 e 5
computador = randint(0, 5)

print('-=-' * 20,'\nVou pensar em um número entre 0 e 5. Tente adivinhar...\n', '-=-' * 20)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')

# Faz o programa fazer uma pausa antes de continuar, aqui dando a impressão que ele está pensando.
sleep(3)
if numero == computador:
    print('Você acertou, abestado! Parabéns, você venceu!')
else:
    print('Sinto muito, mas eu pensei no número {}!'.format(computador))
