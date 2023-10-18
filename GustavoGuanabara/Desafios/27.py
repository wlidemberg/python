"""
    CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMERO E O ULTIMO NOME SEPARADAMENTE
    EX:
    ANA MARIA DE SOUSA
    PRIMERO = ANA
    ULTIMO = SOUSA
"""

n = str(input('Digite o nome e sobrenome: ')).strip()
nome = n.split()

print(len(nome))