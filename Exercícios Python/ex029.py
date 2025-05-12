vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você foi multado!')
    print('Cada Km/h acima de 80 custará R$7,00. Desse modo, sua multa custará R${:.2f}'.format((vel - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')