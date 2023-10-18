"""
    FAÇA UM PROGRMA QUE CALCULE A ÁREA DE UM QUADRADO, SEM SEGUIDA MOSTRE O DOBRO DESTA ÁREA PARA O USUÁRIO

"""

i = float(input("Digite um lado do quadrado: "))
q = i ** 2
quad = q * 2
print('O valor do quadrado é {:.2f} e seu dobro é {:.2f}'.format(q, quad))