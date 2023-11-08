"""
Desenvolva um programa que leia tres seguimentos de retas e diga ao usuário se eles podem ou nao formar um triangulo
"""
print('-=' * 20)
print('Analisador de Segmintos de reta')
print('-=' * 20)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo: ')
else:
    print('Os segmentos acima não podem formar um triangulo')
