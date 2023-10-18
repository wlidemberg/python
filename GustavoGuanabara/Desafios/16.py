"""Crie um programa que leia um número real qualquer pelo teclado e mostre na tela
a sua porção inteira"""

import math
num = float(input("Digite um numero qualquer: \n"))
#print('Este é o número {}!'.format(math.floor(num)))
print('Usando a biblioteca math, o valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))
#math.trunc(n) da um truncate no numero e retorna so a parte inteira


num2 = float(input('Digite um número qualquer: \n'))
print('Sem usar biblioteca, o numero digitado foi {} e sua porção inteira é {}'.format(num2, int(num2)))

