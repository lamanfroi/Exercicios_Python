num = int(input('Digite um numero inteiro: '))
bina = bin(num)[2:]
octal = oct(num)[2:]
hexadeci = hex(num)[2:]

digitex = int(input('Escolha uma das bases para conversão:\n[ 1 ] Binario\n[ 2 ] Octal\n[ 3 ] Hexadecimal\nSua opção: '))
if digitex == 1:
    print('A conversão do número digitado anteriormente para binario é: {}'.format(bina))
elif digitex == 2:
    print('A conversão do número digitado anteriormente para octal é: {}'.format(octal))
elif digitex == 3:
    print('A conversão do número digitado anteriormente para hexadecimal é: {}'.format(hexadeci))
else:
    print('Opção inválida!')