'''Crie um programa que mostre na tela todos os números
pares que estão no intervalo entre 1 e 50.'''
# 2 , 51 , 2 = de 2 a 51 pulando de 2 em 2 (par, dividido por 2 , por isso o num 2)
# 'end=' ' ' mantem na mesma linha

for n in range(2, 51, 2):
    print(n, end=' ')
print('ACABOU')

# or
# if n % 2 == 0:

for n in range(2, 51, 2):
    if n % 2 == 0:
        print(n, end=' ')
print('ACABOU')