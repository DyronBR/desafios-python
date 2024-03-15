from random import choice
from time import sleep

print('\033[36m' + '-=-' * 16 + '\n             Vamos jogar Jokenpô?\n' + '-=-' * 16 + '\033[m')
print('''Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

eu = input('\nQual é a sua jogada? ').strip()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!\n')


possibilidades = ['pedra', 'papel', 'tesoura']

computador = choice(possibilidades)

if eu == '2':
    if computador == 'tesoura':
        print('Você jogou tesoura.\nO computador jogou tesoura. \n\033[33mNós empatamos!\033[m')
    elif computador == 'pedra':
        print('Você jogou tesoura.\nO computador jogou pedra. \n\033[31mDesculpa, mas essa vitória é minha!\033[m')
    elif computador == 'papel':
        print('Você jogou tesoura.\nO computador jogou papel. \n\033[32mParabéns, você ganhou essa!\033[m')
elif eu == '0':
    if computador == 'pedra':
        print('Você jogou pedra.\nO computador jogou pedra. \n\033[33mNós empatamos!\033[m')
    elif computador == 'papel':
        print('Você jogou pedra.\nO computador jogou papel. \n\033[31mDesculpa, mas essa vitória é minha!\033[m')
    elif computador == 'tesoura':
        print('Você jogou pedra.\nO computador jogou tesoura. \n\033[32mParabéns, você ganhou essa!\033[m')
elif eu == '1':
    if computador == 'pedra':
        print('Você jogou papel.\nO computador jogou pedra. \n\033[32mParabéns, você ganhou essa!\033[m')
    elif computador == 'papel':
        print('Você jogou papel.\nO computador jogou papel. \n\033[33mNós empatamos!\033[m')
    elif computador == 'tesoura.':
        print('Você jogou papel.\nO computador jogou tesoura. \n\033[31mDesculpa, mas essa vitória é minha!\033[m')
else:
    print('Você não fez uma escolha válida.')
