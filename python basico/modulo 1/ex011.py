# programa para calcular a quantidade de litros de tinta necessária para pintar uma parede
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
quantidade_tinta = area / 2
print('Sua parede tem a dimensão de {}m x {}m e a área é de {:.2f}m².'.format(largura, altura, area))
print('Para pintar sua parede, você precisará de {:.2f}l de tinta'.format(quantidade_tinta))
