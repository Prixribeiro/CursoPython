#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Qual a quantidade de dias que o carro foi alugado? '))
kmRodados = float(input('Qual a quiantidade de KM rodados: '))
totalDiaria = dias * 60
totalKM = kmRodados * 0.15

totalPagar = totalDiaria + totalKM

print('O total do valor das diárias do veículo ficou em R${:.2f}, o total de KM rodados em R${:.2f},'
      '\ne o total a pagar é de R${:.2f}'.format(totalDiaria, totalKM, totalPagar))