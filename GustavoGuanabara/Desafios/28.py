"""
    Escreva um programa que faça o computador 'Pensar' num numero inteiro de 0 a 5 e peça para o usuario tentar descobrir
    qual foi o numero escolhido pelo computador.
    O programa devera escrever na tela se o usuario venceu ou perdeu.
"""

from random import randint #import um função especifica da biblioteca e não ela inteira
from time import sleep
computador = randint(0,5) # gera um inteiro entre zero e cinco
print('Pensei no numero {}'.format(computador))
print('-=-' * 40) #gera a string 20 vezes
print('Pensei em um número de 0 a 5, tente advinhar...')
print('-=-' * 40) # gera a string 20 vezes)

jogador = int(input('Em que número pensei? -> ')) #armazena a opção ue o jogador escolheu
print('Processando...')
sleep(2)
if jogador == computador: #verfica se o que o jogador digitou é igual ao computador
    print('Parabens, você acertou!!!! Pensamos no número {}'.format(computador))
else:
    print('Eu pensei no número {} e não o {}, infelizmente você errou!!'.format(computador, jogador))
