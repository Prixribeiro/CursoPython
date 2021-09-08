# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1

print('O número digitado foi: {}, seu antecessor é o número {} e seu sucessor é número {}. '.format(num, ant, suc))
