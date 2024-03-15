aproveitamento = {}
gols = []
jogadores = []
while True:
    aproveitamento['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'  Quantos gols na partida {c + 1}: ')))
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = sum(gols)
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        print('Erro. Por favor, digite apenas S ou N.')
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    jogadores.append(aproveitamento.copy())
    gols.clear()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"cod":<4}{"nome":<21}{"gols":<16}{"total":<61}')
for i, v in enumerate(jogadores):
    print(f'{i:<4}{str(v["nome"]):<21}{str(v["gols"]):<16}{str(v["total"]):<61}')
print('--' * 30)
while True:
    cod = int(input('Mostrar os dados de qual jogador? (999 para parar): '))
    if cod < len(jogadores):
        print(f' -- Levantamento do jogador {jogadores[cod]["nome"]}:')
        for i, v in enumerate(jogadores[cod]['gols']):
            print(f'  => Na partida {i + 1}, fez {v} gols.')
        print('--' * 30)
    elif cod >= len(jogadores) and cod != 999:
        print(f'ERRO! Não existe jogador com código {cod}!')
        print('--' * 30)
    if cod == 999:
        break
print('<< VOLTE SEMPRE >>')
