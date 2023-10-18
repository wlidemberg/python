"""
    CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
    -> O NOME COM TODAS AS LETRAS MAIÚSCULAS
    -> O NOME COM TODAS AS LETRAS MINUSCULAS
    -> QUANTAS LETRAS AO TODO SEM CONSIDERAR OS ESPAÇOS
    -> QUANTAS LETRAS TEM O PRIMEIRO NOME
"""

n = str(input('Digite seu nome completo, por favor: ')).strip()
maiusculas = n.upper()
minusculas = n.lower()
quantidade = len(n.replace(" ", ""))
primeiro = n.split()

print('Maiusculas: {}\nMinusculas: {}\n'
      'Quantidade: {}\nNome tem {} letras'.format(maiusculas, minusculas, quantidade, len(primeiro[0])))
