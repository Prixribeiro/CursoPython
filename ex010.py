#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

rs = float(input('Digite o valor em Reais (R$) que deseja converter para dólares: '))
print('Com o valor de R$ {:.2f}, você obterá USD {:.2f}.'.format(rs, rs/5.32))