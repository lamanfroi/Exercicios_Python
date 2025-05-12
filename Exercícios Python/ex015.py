perc = float(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias: '))
pago = (dias*60) + (perc*0.15)
print('Preço a pagar: R${:.2f}'.format(pago))