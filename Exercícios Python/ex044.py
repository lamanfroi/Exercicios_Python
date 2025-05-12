preco = float(input('Qual o preco do produto? '))
parcel = int(input('Se você quer pagar a vista no dinheiro, digite 1.\nSe quiser pagar a vista no cartao, digite 2.\nSe  quiser pagar em 2x no cartao, digite 3.\nSe quiser pagar em 3x ou mais no cartão, digite 4.'))
avis = preco - (preco * 0.1)
aviscart = preco - (preco * 0.05)
parcelado = preco + (preco * 0.2)
if parcel == 1:
    print('Parabéns, você ganhou 10% de desconto, o preço foi de R${:.2f} para R${:.2f}'.format(preco, avis))
elif parcel == 2:
    print('Parabéns, você ganhou 5% de desconto, o preço foi de R${:.2f} para R${:.2f}'.format(preco, aviscart))
elif parcel == 3:
    print('Infelizmente você não ganhou nenhum desconto na sua compra. O preço ficou em R${:.2f}'.format(preco))
elif parcel == 4:
    print('Em 4x ou mais vezes, a compra terá um acréscimo de 20% de juros na compra. O preço ficou em R${:.2f} para R${:.2f}'.format(preco, parcelado))