"""
    João Papo-de-Pescador, homem de bem, comprou um microcomputador para calcular o rendimento diario do seu trabalho.
    Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
    (50 kilos) deve pagar um multa de R$ 4,00 para cada kilo excedente.Jão precisa que você faça um programa que leia
    a variável peso(peso dos peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos alem do limite
    e na variável multa o valor da multa que João deve pagar. Imprima os dados do programa com as mensagens adequadas.
"""

nome = str(input('Digite o nome do pescador: ')).strip()
peso = float(input('Digite a quantidade de kilos de peixe: '))

def calcula_peso_excedente(peso):
    if peso > 50.0:
        excesso = peso - 50
        multa = excesso * 4.
        print(f'A quantidade que {nome} pescou foi de {peso} kilos e excedeu {excesso} com um multa de R$ {multa}')
    else:
        print(f'A quantidade que {nome} pescou foi de {peso} kilos e não excedeu, não gerando multa!')

calcula_peso_excedente(peso)
