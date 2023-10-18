"""
    CRIE UM PROGRAMA QUE LEIA O NOME DE UM CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME 'SANTO'.
"""

c = str(input('Digite um nome de uma cidade: ')).strip()
print(c[:5].upper() == 'SANTO')


"""cidade = c.upper().split()
if 'SANTO' in cidade[0]:
    print('a Cidade {} começa com Santo '.format(c))
else:
    print('A cidade {} não começa com Santo'.format(c))"""

p1 = float(input('Digite o valor do primeiro produto: '))
p2 = float(input('Digite o valor do segundo produto: '))

prod1 = ((p1 * 4.5) / 100) + p1
prod2 = ((p2 * 4.5) / 100) + p2

print(prod1)
print(prod2)