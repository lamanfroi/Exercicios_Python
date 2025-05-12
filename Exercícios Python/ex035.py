r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 or r1 + r3 > r2 or r2 + r3 > r1:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo.')