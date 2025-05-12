reais = float(input('Quantos reais você tem? R$'))
dolar = reais/6.18
euro = reais/6.38
print('com R${} você pode comprar apenas ${:.2f} dólares.'.format(reais, dolar))
print('Com R${} você pode comprar apenas ${:.2f} euros.'.format(reais, euro))