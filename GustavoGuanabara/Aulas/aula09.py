"""
    MANIPULAÇÃO DE STRINGS
"""

frase = 'Curso em Video Python'
print(frase[3:10:2])#primeiro número (inicio) - segundo número (fim e não inclui essa posição) - terceiro número (saltos entre a sequencia)
print(frase[:5])#inicio ate a posição cinco, sendo essa não incluida e a omissão da numeração de incio indica que sera do zero
print(frase[5:])#inicia no cinco e vai ate o final devido a omissão do segundo número
print(frase[::2])#pega a sequencia inteira e pula de dois em dois
print(frase.count('o'))#conta quantas vezes aparece o 'o' dentro da sequencia
print(len(frase))#Conta o tamanho total da sequencia - 21 contando os espaços
print(frase.strip())#remove os espaços no inicio e no final da frase
print(frase.replace('Python', 'Android'))#Troca a palavra Python por Android
print(frase.replace('Android', 'Python'))
print('Curso' in frase)# verifica se a palavra existe dentro da sequencia e retorn um booleano
print(frase.find('Curso'))#retorna a posição que esta a palavra na sequencia
print(frase.split())#cria um lista com o conjunto de palavras divididas pelos espaços




#Impressão de uma grande quantidade de texto poderá ser feito com print("""Tres aspas inicio e fim""")
print("""Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing 
industries for previewing layouts and visual mockups.""")
