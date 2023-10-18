"""
    CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER PELO TECLADO E MOSTRE:
    -> QUANTAS VEZES A LETRA 'A' APARARECE
    -> EM QUE POSIÇÃO ELA APARECE NA PRIMEIRA VEZ
    -> EM QUE POSIÇÃO ELA APARECE NA ULTIMA VEZ
"""

frase = str(input("Digite qualquer frase: ")).strip().upper()
print('A letra a aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra a apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra a apareceu na posição {}'.format(frase.rfind('A')+1))