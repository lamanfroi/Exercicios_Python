from time import sleep

c = 10
for c in range(10, 0, -1):
    print('Contagem regressiva para o estouro de fogos de artifício: {}'.format(c))
    sleep(1)
print('FIM!')