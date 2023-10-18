"""
    FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS CÓDIGOS SEPARADOS
    EX:
        DIGITE UM NÚMERO 1834
        UNIDADES: 4
        DEZENAS: 3
        CENTENAS: 8
        MILHAR: 1
"""

n = int(input('Digite um numero qualquer de 0 à 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))
