# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número para saber seu dobro, triplo e raiz quadrada: '))
print('O dobro do valor digitado é {}'.format(n*2))
print('O triplo do valor digitado é {}'.format(n*3))
print('A raiz quadrada do valor digitado é {:.2f}' .format(n ** (1/2)))