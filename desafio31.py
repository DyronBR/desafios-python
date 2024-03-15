distancia = float(input('Digite a distância da viagem em KM: '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    print('O valor da passagem será de R${:.2f}.'.format(distancia * 0.50))

else:
    print('O valor da passagem será de R${:.2f}.'.format(distancia * 0.45))

# outro modo de fazer a mesma coisa mais simplificado

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
