from random import randint
from time import sleep
itens = 'Pedra', 'Papel',' Tesoura'
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
sleep(3)
if computador == 0: #Computador jogou Pedra
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('O JOGADOR VENCE!')

    elif jogador == 2:
        print('O COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #Jogou papel
    if jogador == 0:
        print('O JOGADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O JOGADOR VENCE!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #Jogou Tesoura
    if jogador == 0:
        print('O JOGADOR VENCE!')
    elif jogador == 1:
        print('O COMPUTADOR VENCE!')

    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
