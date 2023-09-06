'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.''' #Curso do Gustavo Guanabara

salario = float(input('Qual é o valor do seu salário? '))
if salario > 1250:
    aumento = salario * 10 / 100
    novosalario = salario + aumento
    print('Seu salário teve um aumento de 10%,no valor de {}, o seu salário atual é {}'.format(aumento, novosalario))
if salario <= 1250:
    aumento = salario * 15 / 100
    novosalarion = salario + aumento
    print('Seu salário teve um aumento de 15%, no valor de {}, o seu salário atual é {}'.format(aumento, novosalarion))


salario = float(input('Qual é o valor do seu salário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)

else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))