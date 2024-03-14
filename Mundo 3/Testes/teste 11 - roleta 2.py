from random import choice
from time import sleep

color={
    'preto':'\033[30;47m', #
    'vermelho':'\033[31;47m', #
    'verde':'\033[32;47m', #
    'amarelo':'\033[33;47m', #
    'azul':'\033[34;47m', #
    'roxo':'\033[35;47m', #
    'ciano':'\033[36;47m', #
    'padrão':'\033[30;47m'
}
roulette=[
    '1 | Girar novamente', # preto
    '2 | BOOM', # azul
    '3 | Pergunta', # verde
    '4 | Passe a vez', # amarelo
    '5 | X2 Pergunta', # roxo
    '6 | BOOM', # padrão
    '7 | X3 Pergunta', # ciano
    '8 | Pergunta' # vermelho
]
escolha=''
while True:
    cor=0
    time=0
    while True:
        if escolha==roulette[0]:
            break
        option=str(input('Digite "Começar" para girar a roleta\n-> ').lower())
        if 'começar' in option:
            break
        else:
            print('Ops acho que você escrevou errado... Tente novamente.')
    # ┌ ┐ └ ┘ │
    print(f'''{color["padrão"]}
 ┌{"─"*40}┐
 │{"Girando a roleta":^40}│
 └{"─"*40}┘''')
    print('─'*44)
    for i in range(100):
        escolha=choice(roulette)
        if escolha==roulette[0]:
            cor=color['preto']
        elif escolha==roulette[1]:
            cor=color['azul']
        elif escolha==roulette[2]:
            cor=color['verde']
        elif escolha==roulette[3]:
            cor=color['amarelo']
        elif escolha==roulette[4]:
            cor=color['roxo']
        elif escolha==roulette[5]:
            cor=color['padrão']
        elif escolha==roulette[6]:
            cor=color['ciano']
        elif escolha==roulette[7]:
            cor=color['vermelho']
        print(f'\r{cor}<[{escolha:^40}]>',end='')
        sleep(time)
        time+=0.0025
    print(f'{color["padrão"]}')
    print('─'*44)
    if escolha==roulette[0]:
        for i in range(5,0,-1):
            print(f'\rO item escolhido foi " {escolha} " então a roleta girará novamente em {color["verde"]}{i}{color["padrão"]}',end='')
            sleep(1)
        print('')
        print('─'*44)
    while True:
        if escolha==roulette[0]:
            break
        option=str(input('Você deseja girar a roleta novamente? [s/n] '))
        if option not in 'sn':
            print(f'{color["vermelho"]}Opção inválida, tente digitar S ou N.{color["padrão"]}')
        else:
            break
    if option in 'Nn':
        break