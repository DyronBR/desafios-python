from datetime import date

# Em seguida, obtemos o ano a partir da data encontrada.
atual = date.today().year

nome = input('Qual o seu nome? ')
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
saldome = atual + (18 - idade)
saldoma = atual - (idade - 18)

if idade < 18:
    print('{} tem {} anos em {}. \nSendo assim, ainda falta {} ano(s) para ele se alistar.'
          .format(nome, idade, atual, 18 - idade))
    print('Logo você deverá se alistar no ano {}'.format(saldome))
elif idade == 18:
    print('{} tem {} anos em {}. \nSendo assim, está na hora de se alistar.'.format(nome, atual, idade))
elif idade > 18:
    print('{} tem {} anos em {}. \nSendo assim, já passou {} ano(s) do prazo para se alistar.'.format(nome, idade, atual,
                                                                                                    idade - 18))
    print('Logo, você deveria ter se alistado em {}'.format(saldoma))
