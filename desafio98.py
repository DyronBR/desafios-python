from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(0.3)
    elif inicio > fim:
        for c in range(inicio, fim - 1, passo * -1):
            print(c, end=' ')
            sleep(0.3)
    print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é Sua Vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
print('-=' * 30)
