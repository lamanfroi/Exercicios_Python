n = str(input('Digite seu nome completo: ')).title()
nome = n.split()
pnome = nome[0]
unome = nome[-1]
print('Muito prazer em te conhecer, {}!!'.format(n))
print('Seu primeiro nome é: {}'.format(pnome))
print('Seu último nome é: {}'.format(unome))

#     Metodo Guarana Jesus
#print('Muito prazer em te conhecer, {}!!'.format(n))
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[len(nome)-1]))