from random import randint
num=randint(1,6)
n1=int(input('Escolha um número entre 1 e 6: '))
if num==n1:
    print('Você acertou o número!')
else:
    print('Você errou, o número era {}, tente novamente :('.format(num))
