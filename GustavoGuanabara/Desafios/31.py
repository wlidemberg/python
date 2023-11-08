"""
    Desenvolva um programa que pergunte a distancia de um viagem em km.
    calcule o preço da passagem sendo 0,50 para as distancias ate 200km por km e 0,45 para distancias acima de 200km
"""
'''
***********************************************************************************************************************
if simplificado
passagem = distancia * 0.5 if distancia <= 200 else distancia *0.45
***********************************************************************************************************************
'''


distancia = float(input('Digita a distancia do destino: '))
if distancia <= 200:
    passagem = distancia * 0.5
    print('-=-' * 10)
    print('Preço da viagem')
    print('-=-' * 10)
    print('Distancia da viagem {}km'.format(distancia))
    print('-' * 30)
    print('Valor da passagem R$ {:.2f}'.format(passagem))
    print('-' * 30)
    print('-' * 30)
elif distancia > 200:
    passagem = distancia * 0.45
    print('-=-' * 10)
    print('Preço da viagem')
    print('-=-' * 10)
    print('Distancia da viagem {}km'.format(distancia))
    print('-' * 30)
    print('Valor da passagem R$ {:.2f}'.format(passagem))
    print('-' * 30)
    print('-' * 30)
else:
    print('Valor invalido')