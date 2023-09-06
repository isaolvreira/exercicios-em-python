''''Refaça o DESAFIO 9, mostrando a tabuada de um número que o
usuário escolher, só que agora utilizando um laço for.'''

# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
# num =int(input('Digite um número para ver sua tabuada: '))

tabuada = int(input('Digite o número da tabuada que você quer: '))
for count in range(0, 10):
 print('{} x {:2} = {}'.format(tabuada, count+1, (tabuada * (count+1))))


num = int(input('Digite um número da tabuada que você quer: '))
for count in range(1, 11):
 print('{} x {:2} = {}'.format(num, count, num*count))

 tabuada = int(input('Digite a tabuada que você deseja: '))
 for c in range(0, 11):
  print('{} x {:2} = {}'.format(tabuada, c, (c * tabuada)))
