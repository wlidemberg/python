"""
    Tendo como dado de entrada a altura(h) de uma pessoa, construa um algoritmo que calcule se peso ideal, utilizando
    as seguintes fórmulas:
    a) para homens: fórmula: (72.7 * h) - 58
    b) para mulheres: fórmula: (62.1 * h) - 44.7=
"""

h = float(input('Digite sua altura: '))
sexo = int(input('Escolha 1) - masculino ou 2) - Feminino: '))

def calcular_peso_ideal(altura, sexo):
    if sexo == 1:
        resultado = 72.7 * altura - 58
        sexo = 'Masculino'
        return resultado, sexo
    else:
        resultado = 62.1 * h - 44.7
        sexo = 'Feminino'
        return resultado, sexo

peso_ideal = calcular_peso_ideal(h, sexo)
print(f'O peso ideal para uma pessoal do sexo {peso_ideal[1]} com {h} altura é de {peso_ideal[0]:.2f} kg')
