r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('As retas podem formar um triângulo!')
    if r1 == r2 != r3 and r1 == r3 != r2 and r2 == r3 != r1:
        print('E um triangulo isosceles')
    elif r1 == r2 == r3:
        print('E um triangulo equilatero')
    elif r1 != r2 != r3:
        print('E um triangulo escaleno')
else:
    print('As retas não podem formar um triângulo.')