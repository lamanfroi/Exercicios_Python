from time import sleep

print('-=' * 10)
valorUm = int(input('Digite o primeiro valor: '))
valorDois = int(input('Digite o segundo valor: '))
sleep(2)
escolha = int

while escolha != 5:
    print('-=' * 10)
    print('MENU!!!\n[1] Somar\n[2] Multiplicar\n[3] maior número\n[4] novos números\n[5] Sair do programa\n')
    escolha = int(input('Qual a sua escolha? '))

    if escolha == 1:
        print('Somando os números...')
        sleep(1)
        print('A soma deu: {}'.format(valorUm + valorDois))
    elif escolha == 2:
        print('Multiplicando os números...\n')
        sleep(1)
        print('A multiplicação dos números deu: {}'.format(valorUm * valorDois))
    elif escolha == 3:
        print('Descobrindo qual valor é maior...')
        sleep(1)
        if valorUm > valorDois:
            print('O maior valor é o {}.'.format(valorUm))
        elif valorDois > valorUm:
            print('O maior valor é o {}.'.format(valorDois))
    elif escolha == 4:
        print('Escolha os novos números.\n')
        valorUm = int(input('Para o primeiro número, qual valor você quer? '))
        valorDois = int(input('Agora para o segundo número... Qual valor você quer? '))
    else:
        print('Você escolheu um número errado.')
print('Você saiu do programa.')