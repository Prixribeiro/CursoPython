#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
totalArea = largura * altura
tinta = totalArea / 2

print('Sua parede tem a dimensão de {} x {}, e sua área é de {}m².'.format(largura, altura, totalArea))
print('Para pintar a área total de sua parede, você irá precisar de {} litros de tinta'. format(tinta))