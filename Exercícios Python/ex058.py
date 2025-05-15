from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar... ')
print('-=-' * 20)

sleep(1.5)
print('\nPROCESSANDO...\n')
sleep(1.5)

jogador = int
sorteio = randint(0, 10)
palpites = 0

while jogador != sorteio:
    palpites += 1
    jogador = int(input('Qual seu palpite? '))
    if jogador < sorteio:
        print('Mais... Tente mais uma vez.')
    elif jogador > sorteio:
        print('Menos... Tente mais uma vez.')
print('Você conseguiu! A máquina havia escolhido o número: {}. Você demorou {} palpites para acertar.'.format(sorteio, palpites))





'''
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == computador
        acertou == True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} palpites!'.format(palpites))

'''