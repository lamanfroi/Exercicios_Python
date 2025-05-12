num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# Verificando quem é menor
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
print('O menor valor digitado foi: {}'.format(menor))
# Verificando quem é o maior
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('O maior valor digitado foi: {}'.format(maior))

'''if num1 > num2 and num1 > num3:
    print('O maior número é o primeiro, {}'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior número é o segundo, {}'.format(num2))
elif num3 > num1 and num3 > num2:
    print('O maior número é o terceiro, {}'.format(num3))
if num1 < num2 and num1 < num3:
    print('O menor número é o primeiro, {}'.format(num1))
elif num2 < num1 and num2 < num3:
    print('O menor número é o segundo, {}'.format(num2))
elif num3 < num1 and num3< num2:
    print('O menor número é o terceiro, {}'.format(num3))'''