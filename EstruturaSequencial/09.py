"""
    FAÇA UM PROGRAMA QUE QUE PEÇA A TEMPERATURA EM GRAUS FAHRENHEIT, E TRANSFORME E MOSTRE EM GRAUS CELSIUS.
"""

fah = float(input("Digite o valor em Fahrenheit; "))
celsius = 5 * ((fah-32)/9)
print('A temperetura de {:.2f} Fº é de {:.2f} Cº'.format(fah, celsius))