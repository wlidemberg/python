"""
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar o limite de 80km, mostra uma mensagem dizendo que ele foi multado.
    a multa vai custar R$ 7,00 por cada km ultrapassado
"""

velocidade = float(input('Digite a velocidade do veiculo: '))
if velocidade > 80:
    limite = velocidade - 80
    multa = limite * 7
    print('Você ultrapassou o limite de velocidade em {}km foi multado em  R$ {:.2f}'.format(limite, multa))
else:
    print('Parabens, voce estava dentro da velocidade limite!')