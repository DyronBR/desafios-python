km = float(input('Digite a distancia, em KM, percorrida: '))
dia = int(input('Digite a quantidade de dias que ele foi alugado: '))
valor = km * 0.15 + 60 * dia
print('O valor pago por {} dias de aluguel e {}Km percorridos é de R${:.2f}.'.format(dia, km, valor))
