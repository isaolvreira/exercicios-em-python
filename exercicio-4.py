'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('Você nasceu no ano {}, de acordo com sua idade que é {} '.format(nasc, idade))
    print('Sua categoria é Mirim.')
elif idade <= 14:
    print('Você nasceu no ano {}, de acordo com sua idade que é {}'.format(nasc, idade))
    print('Sua categoria é Infantil.')
elif idade <= 19:
    print('Você nasceu no ano {}, de acordo com sua idade que é {}'.format(nasc, idade))
    print('Sua categoria é Júnior.')
elif idade <= 25:
    print('Você nasceu no ano {}, de acordo com sua idade que é {}'.format(nasc, idade))
    print('Sua categoria é Sênior.')
else:
    print('Você nasceu no ano {}, de acordo com sua idade que é {}'.format(nasc, idade))
    print('Sua categoria é Master.')
