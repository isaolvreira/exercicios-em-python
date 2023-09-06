'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''

# soma, contador (+1)
s = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        s = s + num
        count = count + 1
print('Você informou {} numeros pares ,e a soma foi {}.'.format(count, s))
