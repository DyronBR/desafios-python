from time import sleep


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    m = 0
    for c, v in enumerate(num):
        if c == 0:
            m = v
        else:
            if m < v:
                m = v
        print(v, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
