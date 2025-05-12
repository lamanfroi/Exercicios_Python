from time import sleep

numero = int(input('Qual número você quer ver a tabuada? '))

for n in range(1, 11):
    resultado = numero * n
    print('A tabuada deste número é: {}'.format(resultado))
    sleep(1)
