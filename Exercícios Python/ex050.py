somaPares = 0

for i in range(6):
    numero = int(input(f'Digite o {i+1}º número: '))
    if numero % 2 == 0:
        somaPares += numero

print('A soma dos números pares é: {}'.format(somaPares))