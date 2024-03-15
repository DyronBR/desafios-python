aproveitamento = {}
aproveitamento['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
gols = []
for c in range(0, partidas):
    gols.append(int(input(f'  Quantos gols na partida {c + 1}: ')))
aproveitamento['gols'] = gols[:]
aproveitamento['total'] = sum(gols)
print('-=' * 30)
print(aproveitamento)
print('-=' * 30)
for k, v in aproveitamento.items():
    print(f'o campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {aproveitamento["nome"]} jogou {len(aproveitamento["gols"])} partidas.')
for i, v in enumerate(aproveitamento['gols']):
    print(f'  => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')
