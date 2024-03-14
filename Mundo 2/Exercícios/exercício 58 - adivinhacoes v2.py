from random import randint
print('Jogo de adivinhações 2!')
print('==='*10)
n1=str(input('Você deseja iniciar o jogo? [s/n] '))
if n1=='s' or n1=='sim':
    print('==='*10)
    num=randint(0,10)
    print('O computador escolheu um número entre 1 e 10, tente acerta-lo.')
    tent=n2=0
    tentativa=False # varievel falsa
    while not tentativa: # enquanto variavel não for vdd:
        n2=int(input('Escolha um número: '))
        if n2==num:
            tentativa=True # se o jogador acertou variavel=vdd
        else:
            print('{}Você errou :( \nTente novamente.{}'.format('\033[31m','\033[37m'))
            if n2>num:
                print('Dica: menos!')
            else:
                print('Dica: mais!')
        if n2>10:
            print('Esse número é muito grande. Digite um número até 10.')
        tent+=1
    print('Parabéns! Você acertou em {} tentativas. O computador também escolheu {}.'.format(tent, num))
else:
    print('Ok, tenha um bom dia!')
