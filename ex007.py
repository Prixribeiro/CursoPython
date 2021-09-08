#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite o valor da sua nota de matemática: '))
n2 = float(input('Digite o valor da sua nota de Português: '))
media = (n1 + n2) / 2

print('A média do aluno é {}' .format(media))
