"""
    Faça um programa que peça 2 numeros e um numero real.Calcule e mostre:
    a) O produto do dobro do primeiro com a metade do segundo.
    b) A soma do triplo do primeiro com o terceiro
    c) O terceiro elevado ao Cubo
"""
from typing import Union, Any

n1 = int(input('Digite um número inteiro :'))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))

def calculo_dobro_metade(num_1, num_2):
    resultado: Union[Union[int, float], Any] = (num_1 * 2) * (num_2 / 2) #pep484
    return resultado

def calculo_soma_triplo(num_1, num_3):
    resultado = (num_1 * 3) + num_3
    return resultado
def calculo_cubo(num_3):
    resultado = num_3 ** 3
    return resultado

dobro_metade = calculo_dobro_metade(n1, n2)
soma_triplo = calculo_soma_triplo(n1, n3)
cubo = calculo_cubo(n3)
print(f'O produto do dobro do primeiro número com a metade do segundo número é {dobro_metade}')
print(f'A Soma do triplo do primeiro com terceiro {soma_triplo}')
print(f'O Cubo do terceiro {cubo}')



