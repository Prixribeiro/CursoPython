#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

t = int(input('Digite o número que deseja saber a tabuada: '))

print('='*50)
print('Tabuada do {}'.format(t))
print('{} x {:2} = {}'.format(t, 1, t*1))
print('{} x {:2} = {}'.format(t, 2, t*2))
print('{} x {:2} = {}'.format(t, 3, t*3))
print('{} x {:2} = {}'.format(t, 4, t*4))
print('{} x {:2} = {}'.format(t, 5, t*5))
print('{} x {:2} = {}'.format(t, 6, t*6))
print('{} x {:2} = {}'.format(t, 7, t*7))
print('{} x {:2} = {}'.format(t, 8, t*8))
print('{} x {:2} = {}'.format(t, 9, t*9))
print('{} x {:2} = {}'.format(t, 10, t*10))

print('='*50)
