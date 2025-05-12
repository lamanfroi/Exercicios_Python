c = 1
for c in range(1, 500):
     if c % 2 != 0 and c % 3 == 0:
         resultado = c + c
print('A soma de todos os números ímpares que são multiplos de 3 são: {}'.format(resultado))