"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
    um triangulo retangulo, calcule o mostre o comprimento da hipotenusa.
    Para calcular a HIPOTENUSA usamos o Teorema de Pitagorás:
    hipotenusa² = catetoOposto² + catetoAdjacente²
"""
from math import hypot
catetoOposto = float(input("Digite o Valor do Cateto Oposto:  "))
catetoAdjacente = float(input("Digite o valor do Cateto Adjacente:  "))

hi = hypot(catetoOposto, catetoAdjacente)

'''def calculoHipotenusa():
    hi = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
    return hi
resultado = calculoHipotenusa()'''
print('O valor do Cateto Oposto é {}'
      'O valor do Cateto Adjacente é {}'
      'O valor da Hipotenusa e {:.2f}'.format(catetoOposto, catetoAdjacente, hi))
