from random import randint
from time import sleep
n1=str(input('{}Vamos jogar jokenpô? [s/n] \n'.format('\033[31m')).strip().lower())
#num=1
num=randint(1,3)
if n1=='s' or n1=='sim':
    print('{}---'.format('\033[35m')*10)
    n2=str(input('''{}Escolha pedra, papel, ou tesoura.
    [1] Pedra
    [2] Papel
    [3] Tesoura
    {}'''.format('\033[32m','\033[35m')).strip().lower())
    sleep(0.4)
    print('JO')
    sleep(0.4)
    print('KEN')
    sleep(0.4)
    print('PÔ!')
    sleep(0.4)
    if n2=='1' or n2=='pedra':
        n3=1 # pedra
        if num==1:
            print('{}O computador escolheu pedra.'.format('\033[33m'))
            print('O jogo empatou!') # os dois escolheram pedra
        elif num==2:
            print('{}O computador escolheu papel'.format('\033[31m'))
            print('Você perdeu!') #o computador escolheu papel
        elif num==3:
            print('{}O computador escolheu tesoura.'.format('\033[32m'))
            print('Você ganhou!') #o computador escolheu papel
    elif n2=='2' or n2=='papel':
        n3=2 # papel
        if num==1:
            print('{}O computador escolheu pedra.'.format('\033[32m'))
            print('Você ganhou!') # o computador escolheu pedra
        elif num==2:
            print('{}O computador escolheu papel.'.format('\033[33m'))
            print('O jogo empatou!') # os dois escolheram papel
        elif num==3:
            print('{}O computador escolheu tesoura.'.format('\033[31m'))
            print('Você perdeu!') # o computador escolheu tesoura
    elif n2=='3' or n2=='tesoura':
        n3=3 # tesoura
        if num==1:
            print('{}O computador escolheu pedra.'.format('\033[31m'))
            print('Você perdeu') # o computador escolheu pedra
        elif num==2:
            print('{}O computador escolheu papel.'.format('\033[32m'))
            print('Você ganhou!') # o computador escolheu papel
        elif num==3:
            print('{}O computador escolheu tesoura.'.format('\033[33m'))
            print('O jogo empatou!') # os dois escolheram tesoura
elif n1=='n' or n1=='nao' or n1=='não':
    print('{}---'.format('\033[35m')*10)
    print('{}Ok. Tenha um bom dia.'.format('\033[36m'))
