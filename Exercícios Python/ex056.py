maiorIdade = 0
nomeVelho = 0
mediaIdade = 0
somaIdade = 0

for p in range(1, 5):
    print('-------- {}a PESSOA -------'.format(p))
    nome = str(input('Nome: ')).strip().lower()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().lower())
    somaIdade += idade

    if p == 1 and sexo in 'm':
        maiorIdadeDeHomem = idade
        nomeVelho = nome
    if sexo in 'm' and idade > maiorIdadeDeHomem:
        maiorIdadeDeHomem = idade
        nomeVelho = nome
    if sexo in 'f' and idade < 20:
        totalMulher =+ 1

mediaIdade = somaIdade /4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdade, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalMulher))