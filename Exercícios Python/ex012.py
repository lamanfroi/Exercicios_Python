preco = float(input('Digite o preço do produto: R$'))
desconto = float(preco*0.05)
vt = preco - desconto
print('O preço do produto com o desconto de 5% ficou R${:.2f}'.format(vt))