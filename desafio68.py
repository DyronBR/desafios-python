from random import randint
print('-=-' * 10)
print('Vamos jogar par ou impar?')
print('-=-' * 10)
total_vitorias = PC = 0
while True:
    num = int(input('Digite o número escolhido: '))
    usuario = str(input('Digite sua escolha [P/I]: ')).upper().strip()[0]
    while usuario not in 'PpIi':
        usuario = str(input('Digite sua escolha [P/I]: ')).upper().strip()[0]
    computador = randint(0, 10)
    print('---' * 10)
    if usuario == 'I':
        PC = 'PAR'
    else:
        PC = 'IMPAR'
    if (num + computador) % 2 == 0:
        resultado = 'P'
        res = 'PAR'
    else:
        resultado = 'I'
        res = 'IMPAR'
    print(f'Eu joguei {computador} e você {num}. A soma deu {computador + num} o que é {res}.')
    if usuario == resultado:
        total_vitorias += 1
        print('---' * 10)
        print('Parabéns, você ganhou.\nVamos jogar novamente...')
        print('---' * 10)
    if usuario != resultado:
        break
print('---' * 10)
print('GAME OVER.')
print(f'\033[31mVocê ganhou {total_vitorias} vezes\033[m')
print('---' * 10)
