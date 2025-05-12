nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media < 7.0:
    print('RECUPERACAO')
elif media > 7.0:
    print('APROVADO')
