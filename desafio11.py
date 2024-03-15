la = float(input('Qual a largura da parede, em metros? '))
al = float(input('Qual a altura da parede, em metros? '))

ar = la * al
tn = ar / 2

print('A área total da parede é {:.2f} m². \nSendo assim, '
      'será necessário {:.3f} l de tinta para pintá-la.'.format(ar, tn))
