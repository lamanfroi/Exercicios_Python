salario = float(input('Qual o seu salário? '))
if salario > 1250:
    prim_sal = salario + (salario * 0.1)
    print('Seu salário passou de R${:.2f} para R${:.2f}'.format(salario, prim_sal))
else:
    seg_sal = salario + (salario * 0.15)
    print('Seu passou de R${:.2f} para R${:.2f}'.format(salario, seg_sal))

'''     Método Guaravita
salário = float(input('Qual é o salário do funcionário? R$))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
'''