from math import sqrt, hypot

co = float(input('Digite o cateto oposto do triângulo: '))
ca = float(input('Digite o cateto adjacente do triângulo: '))

# Modo 01
hi = sqrt(co * co + ca * ca)
# Modo 02
hi2 = hypot(co, ca)

print('A hipotenusa desse triângulo é {:.2f}'.format(hi))
print('A hipotenusa desse triângulo é {:.2f}'.format(hi2))