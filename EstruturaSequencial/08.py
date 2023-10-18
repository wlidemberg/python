"""
    FAÇA UM PROGRAMA QUE PERGUNTE O QUANTO VC GANHA POR HORA E O NÚMERO DE HORAS TRABALHADAS NO MES. CALCULE
    E MOSTRE O TOTAL DE SEU SÁLARIO NO REFERIDO MES
"""
valorHora = float(input("Informe o valor de Salario/Hora: "))
quantidadeHora = float(input("Informe a quantidade de horas trabalhadas no mes: "))


def calcula():
    """vhora = (valorHora / 60) * valorHora
    qhora = (quantidadeHora / 60) * quantidadeHora"""
    salario = valorHora * quantidadeHora
    return salario

salarioMes = calcula()
print("O valor de salario do mês 10/2023 é de R$ {:.2f}".format(salarioMes))

