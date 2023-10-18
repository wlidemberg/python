"""
    CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM 'SILVA' NO NOME
"""

nome = str(input("Digite o nome e sobrenome do usuário: "))
contem = 'SILVA' in nome.upper()
if contem == True:
    print(f'O nome {nome} tem Silva')
else:
    print(f'O nome {nome} não tem Silva')