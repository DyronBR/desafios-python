def voto(ano=0):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não pode votar.'
    elif 16 >= idade < 18 or idade > 70:
        return f'Com {idade} anos: Voto opcional.'
    else:
        return f'com {idade} anos: Voto Obrigatório.'


ano = int(input('Digite o ano de nascimento: '))
print(f'{voto(ano)}')
