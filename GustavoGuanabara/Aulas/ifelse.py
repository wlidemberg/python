from django.template.defaultfilters import upper

tempo = int(input('Digite quantos anos tem seu carro? '))

if tempo <= 3:
    print('O seu carro é novo pois so tem {} anos'.format(tempo))
else:
    print('O seu carro é velho pois já tem {} anos'.format(tempo))
print('__________FIM__________')

nome = str(input('Qual o seu nome? ')).strip()
if nome == 'Wlidemberg':
    print('Olá srº {}, estamos aguardando na sala de reuniões!'.format(nome))
else:
    print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda Nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(m))
if m >= 6:
    print('Sua media está boa, Parabens!')
else:
    print('Sua media precisa melhorar, estude mais!')