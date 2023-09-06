'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''
# Não entendi muito bem o 'cont', de resto eu entendi!
# s += n Ou s = s + n a soma vai ser a soma = soma + quantidade de n
cont = 0  #Conta +1
s = 0     #ACUMULADOR - somando mais um, multiplicando,etc.

for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1 # cont += 1
        s += n
        print(n, end=' ')
print('O somatório entre todos os {} valores é {}'.format(cont, s))

