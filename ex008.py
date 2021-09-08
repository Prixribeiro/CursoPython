#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite um valor em metros para converter para centímentros e milímetros: '))
cent = n * 100
mili = n * 1000

print(' {}m é equivalente a {:.0f}cm ou {:.0f}mm.'.format(n, cent, mili))
