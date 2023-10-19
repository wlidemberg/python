"""
    FAÇA UM PROGRAMA QUE RECEBA UM TEMPARATURA EM CELSIUS E CONVERTA E MOSTRE EM FAHRENHEIT
"""
c = float(input("Digite uma temperatura em Celsius: "))
f = c * 1.8 + 32

print('O valor recebido em graus {:.2f} Cº corresponde a {:.2f} Fº'.format(c, f))
