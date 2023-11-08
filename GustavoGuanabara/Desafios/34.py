"""
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    para salários superior a R$ 1.125,00 o aumento é de 10%
    para salários inferior a R$ 1.125,00 o aumento e de 15%
"""
salario = float(input('Digite o salario a ser reajustado: '))
if salario < 1125:
    reajuste = (salario * .15) + salario
else:
    reajuste = (salario * .10) + salario

print('O valor do reajuste foi de R$ {} e seu novo salário  é de R$ {:.2f}'.format((reajuste - salario), reajuste))