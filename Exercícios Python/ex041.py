from datetime import date

nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
elif idade > 20:
    print('MASTER')