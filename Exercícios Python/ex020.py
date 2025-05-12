#from random import shuffle, sample
import random

al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
alall = [al1, al2, al3, al4]
mch = random.sample(alall, k=4)
print('Os alunos escolhidos, em ordem, foram: {}'.format(mch))

''' 
    Método Guanabara

import random

al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
alall = [al1, al2, al3, al4]
random.shuffle(alall)
print('A ordem de apresentação será: {}') 
print(alall)
'''