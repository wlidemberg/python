"""
    Faça um programa que leia um ano qualquer e mostre se ele é um ano bissexto
"""
from datetime import date
from time import sleep

ano = int(input('Digite o ano que quer analisar? Coloque 0 para analisar o ano atual \nano: '))
sleep(3)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))