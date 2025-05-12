import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar... ')
print('-=-' * 20)

pensar = float(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
sorteio = random.randint(0, 5)
if pensar > 5:
    print('Você escolheu um número maior que 5, tente novamente.')
elif pensar < 0:
    print('Você  escolheu um número menor que 0, tente novamente.')
elif pensar == sorteio:
    print('Você acertou!!! O número sorteado foi {}'.format(sorteio))
elif pensar != sorteio:
    print('Você perdeu. O número sorteado foi {}'.format(sorteio))