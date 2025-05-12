primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
progArit = primeiroTermo + (11 - 1) * razao

for i in range(primeiroTermo, progArit, razao):
    print('{}'.format(i), end=' -> ')
print('ACABOU!')


## an = a1 + (n -1).r