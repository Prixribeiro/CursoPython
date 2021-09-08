#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempC = float(input('Quantos graus (ºC) está na sua cidade: '))
tempF = (tempC * 9/5) + 32

print('A temperatura atual {}ºC, em Fahrenheit equivale a {}ºF'.format(tempC,tempF))