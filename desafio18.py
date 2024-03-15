from math import sin, tan, cos, radians

a = int(input('Digite o ângulo a ser calculado: '))
r = radians(a)
s = sin(r)
c = cos(r)
t = tan(r)

print('O seno de {}º é {:.2f}º.\nO cosseno de {}º é {:.2f}º.\nA tangente de {}º é {:.2f}º.'
      .format(a, s, a, c, a, t))
