import random

escolha = str(input('Vamos jogar Jokênpo?\nFaça sua escolha entre pedra, papel ou tesoura: ')).strip().lower()
ped = 'pedra'
pap = 'papel'
tes = 'tesoura'
lista = [ped, pap, tes]
sort = random.choice(lista)

if escolha == sort:
    print('Empate. O computador também escolheu {}.'.format(sort))
elif escolha == pap and sort == tes or escolha == tes and sort == ped or escolha == ped and sort == pap:
    print('Você perdeu! O computador venceu usando a(o) {}'.format(sort))
elif escolha == pap and sort == ped or escolha == tes and sort == pap or escolha == ped and sort == tes:
    print('Você venceu! O computador perdeu usando a(o) {}'.format(sort))