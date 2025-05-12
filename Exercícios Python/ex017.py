from math import hypot, sqrt

cto = float(input('Digite o valor do cateto oposto'))
cta = float(input('Digite o valor do cateto adjacente'))
hipot = hypot(cto, cta)
print('A hipotenusa vai medir {:.2f}'.format(hipot))

#hipot = math.sqrt(cto ** 2 + cta ** 2)
#print('A hipotenusa vai medir {:.2f}'.format(hipot))

#hipot = (cto ** 2 + cta ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hipot))