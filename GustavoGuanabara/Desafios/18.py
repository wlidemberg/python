"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno
cosseno e tangente desse ângulo"""

from math import sin, cos, tan, trunc, radians
angulo = float(input("Digite o ângulo que vc deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo digitado foi {}º\n'
      'O valor de seno é {:.2f}\n'
      'O valor de cosseno é {:.2f}\n'
      'Ovalor da tangente é {:.2f}'.format(trunc(angulo), seno, cosseno, tangente))