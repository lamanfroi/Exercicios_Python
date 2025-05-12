frase = str(input('Digite uma frase: ')).strip().upper()
contar = frase.count('A')
pvez = frase.find('A')
uvez = frase.rfind('A')
print('Quantas vezes apareceu a letra A: {}'.format(contar))
print('Posição em que a letra "A" apareceu a primeira vez: {}'.format(pvez))
print('Posição em que a letra "A" apareceu a última vez: {}'.format(uvez))

#     Metodo Guaravita
#frase = str(input('Digite uma frase: ')).upper().strip()
#print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
#print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
#print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))