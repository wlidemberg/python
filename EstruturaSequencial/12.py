"""
    Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a
    seguinte fórmula: (72.7 * altura) - 58
"""

altura = float(input('Digite a sua altura: '))
def calcula_peso_ideal(altura):
    resultado = (72.7 * altura) - 58
    return resultado

peso_ideal = calcula_peso_ideal(altura)
print(f'O peso ideal para a {altura:.2f} é {peso_ideal:.2f}')