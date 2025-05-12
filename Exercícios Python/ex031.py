dist = float(input('Qual a distância da sua viagem em km? '))
if dist <= 200:
    preco = dist * 0.50
    print('O valor da passagem será de R${:.2f}'.format(preco))
else:
    preco = dist * 0.45
    print('A passagem receberá um desconto, ficando com o valor de R${:.2f}'.format(preco))

'''preco = dist * 0.50 if dist <= 200 else dist * 0.45
print('O preço da viagem será: {:.2f}'.format(preco))'''