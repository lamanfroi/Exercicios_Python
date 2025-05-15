sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Você digitou o carácter errado. Digite novamente [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Você é do sexo masculino!!')
else:
    print('Você é do sexo feminino!!!')