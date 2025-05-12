#from math import radians, sin, cos, tan
import math

angulo = int(input('Digite o ângulo: '))
conv = math.radians(angulo)
sen = math.sin(conv)
cos = math.cos(conv)
tg = math.tan(conv)

print('O seno do ângulo é: {:.2f}'
      '\nO cosseno do ângulo é: {:.2f}'
      '\nA tangente do ângulo é: {:.2f}'
      .format(sen, cos, tg))