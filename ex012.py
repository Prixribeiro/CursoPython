# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual o valor atual do produto: R$ '))
desconto = (produto * 5) / 100
valorFinal = produto - desconto

print('O valor do desconto de 5% é de R$ {:.2f}, e o valor final do produto é de R$ {:.2f}' .format(desconto, valorFinal))
