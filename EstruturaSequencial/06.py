#Faça um programa que peça o raio de um circulo, calcule e mostre sua area

raio = eval(input("Digite o raio do circulo: \n"))

def calculaArea(r):
    area = 3.14 * (raio ** 2)
    return area

print(f'A area de um circulo de acordo com o raio {raio} é de {calculaArea(raio)}')