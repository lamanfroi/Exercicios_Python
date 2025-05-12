valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Voce vai pagar em quantos anos?'))

prestacao = valor / (anos * 12)

if prestacao * 0.3 >= salario:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo negado!')