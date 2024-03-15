print('\033[36m' + '-=-' * 15 + '\n            Calculadora de IMC\n' + '-=-' * 15 + '\033[m\n')

nome = input('Digite o nome: ')
al = float(input('Digite a altura (em metros): '))
pe = float(input('Digite o peso (em kg): '))

imc = pe / al ** 2
print()
if imc < 18.5:
    print('{} está \033[31mabaixo do peso\033[m. \nSeu IMC é {:.2f}.'.format(nome, imc))
elif 18.5 <= imc < 25:
    print('{} está no \033[31mpeso ideal\033[m. \nSeu IMC é {:.2f}.'.format(nome, imc))
elif 25 <= imc < 30:
    print('{} está com \033[31msobrepeso\033[m. \nSeu IMC é {:.2f}.'.format(nome, imc))
elif 30 <= imc < 40:
    print('{} está em estado de \033[31mobesidade\033[m. \nSeu IMC é {:.2f}.'.format(nome, imc))
else:
    print('{} está em estado de \033[31mobesidade mórbida\033[m. \nSeu IMC é {:.2f}.'.format(nome, imc))
