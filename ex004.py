# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n1 = input('Digite qualquer valor: ')

print('O valor digitado é numérico: {}'.format(n1.isnumeric()))
print('O valor digitado é Alfanumérico: {}'.format(n1.isalnum()))
print('O valor digitado é alfabético: {}'.format(n1.isalpha()))
print('O valor digitado está em letras maiúsculas: {}'.format(n1.isupper()))
print('O valor digitado é do tipo: {}'.format(type(n1)))

