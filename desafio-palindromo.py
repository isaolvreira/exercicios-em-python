'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
# SPLIT - LISTA, STRIP - REMOVE ESPAÇOS VAZIOS, UPPER - TRANSFORMA TUDO EM MAIUSCULO
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split() #fiz uma lista
junto = ''.joinlen(palavras) #juntei a lista
inverso = junto[::-1] #fatiamento
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('a frase digitada não é um palindromo!')



