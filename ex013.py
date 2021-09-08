#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salarioAtual = float(input('Informe o salário atual: R$ '))
novoSalário = salarioAtual + (salarioAtual*15/100)

print('Seu salário antigo era de R$ {:.2f}, e com reajuste de 15% passará a ser R$ {:.2f}.' .format(salarioAtual, novoSalário))