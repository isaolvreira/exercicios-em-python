'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
 triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

#Regra de triângulo, cada um lado tem que ser menor que a soma entre os dois lados.
# Pode usar o If dentro de um If. 
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulo!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    if r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO podem formar triangulo!')
