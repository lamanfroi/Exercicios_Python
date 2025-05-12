data = int(input('Digite o ano do seu nascimento: '))
novo = data - 2007
velho = 2007 - data
if data > 2007:
    print('Voce ainda vai se alistar. Faltam {} ano(s) para voce se alistar'.format(novo))
elif data == 2007:
    print('Esta na hora de se alistar')
elif data < 2007:
    print('Passou da hora de voce se alistar. Va a uma junta imediatamente, voce passou {} ano(s)   do tempo'.format(velho))

# from datetime import date
# atual = date.today().year
# nasc = int(input('Ano de nascimento: '))
# idade = atual - nasc
# print('Quem nasceu em {} tem {} anos em {}).format(nasc, idade, atual)
# if idade == 18:
#   print('Você tem que se alistar IMEDIATAMENTE!!!')
# elif idade < 18:
#   saldo = 18 - idade
#   print('Ainda faltam {} anos para o alistamento.'.format(saldo))
#   ano = atual - saldo
#   print('Seu alistamento foi em {}.'.format(ano))
# elif idade > 18:
#   saldo = idade - 18
#   print('Você já deveria ter se alistado há {} anos.'.format(saldo))
#   print('Seu alistamento foi em {}.'.format(ano))