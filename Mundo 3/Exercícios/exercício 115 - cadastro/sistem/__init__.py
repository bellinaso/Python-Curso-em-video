'''
    Criar uma função com while e for que printa o "menu" e depois checa se o valor digitado é inteiro com duas tentativas
    Se for inteiro fecha o laço for, e testa se é um número entre 1 e 3
    Depois só fazer uma função para cada opção do menu'''
import utility
from time import sleep

def menu(msg):
    # teste inteiro
    for i in range(3):
        numint=str(input(msg))

        #gambiarra
        try:
            numint=int(numint)
            if int(numint) and numint>=1 and numint<=3:
                return numint
                break
            else:
                print('\033[31mOpção inválida. Tente digitar um valor de 1 a 3.\033[m')

        except Exception as erro:
            print('\033[31mValor inválido. Tente novamente.\033[m', erro.__class__)
            


def cabeçalhoMenu(msg):

    # cabeçalho do menu
    utility.linha(52,utility.cores(7))
    utility.centralização(52,msg)
    utility.linha(52)
    sleep(0.5)

def textoMenu():
    # texto do menu
    print('''
    {}[1] {}Vizualizar cadastros
    {}[2] {}Cadastrar novas pessoas
    {}[3] {}Finalizar sistema{}
'''.format(utility.cores(3),utility.cores(4),utility.cores(3),utility.cores(4),utility.cores(3),utility.cores(4),utility.cores(7)))
    utility.linha(52)
    sleep(0.5)

def leiaInt(msg):
    while True:
        print(utility.cores(4),end='')
        numint=str(input(msg))
        try:
            numint=int(numint)
        except Exception as erro:
            print('\033[31mValor inválido. Tente novamente.\033[m', erro.__class__)
        else:
            return numint
            break