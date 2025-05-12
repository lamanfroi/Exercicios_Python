n1 = float(input('Em metros, qual é a largura da parede?'))
n2 = float(input('Em metros, qual é a altura da parede?'))
area = n1 * n2
tinta = area / 2
print('Sua parede tem {}x{} e sua área de {} metros quadrados.\nPrecisa-se de {} litros de tinta para pintar a parede.'.format(n1, n2, area, tinta))