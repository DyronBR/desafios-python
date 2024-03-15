from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    s = 0
    for valor in lista:
        if valor % 2 == 0:
            s += valor
    print(f'Somando os valores pares de {números}, temos {s}.')


# Programa Principal
números = []
sorteia(números)
somapar(números)
