vel = float(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print('O limite de velocidade desse percurso é 80km/h.\n'
          'Você transitava a {}km/h, e foi multado no valor de R${:.2f}'.format(vel, multa))
else:
    print('Parabéns. Você estava a {}Km/h. Sendo assim, não ultrapassou os limites de velocidade!'.format(vel))
print('Tenha um bom dia! Dirija com segurança!')
