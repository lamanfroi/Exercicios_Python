from datetime import date

dataAtual = date.today().year
totmaior = 0
totmenor = 0

for pessoas in range(7):
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = dataAtual - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoas atingiram a maioridade.'.format(totmaior))
print('{} pessoas ainda não atingiram a maioridade.'.format(totmenor))