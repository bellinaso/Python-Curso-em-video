def isfloat(msg):
    while True:
        numfloat=str(input(msg))
        try:
            return float(numfloat)
            break
        except:
            print('\033[31mValor inválido. Tente novamente.\033[m')


def isint(msg):
    while True:
        numint=str(input(msg))
        try:
            return int(numint)
            break
        except:
            print('\033[31mValor inválido. Tente novamente.\033[m')


msgfloat=isfloat('Digite um número real: ')
msgint=isint('Digite um número inteiro: ')
print(f'Você digitou o número real {msgfloat} e o número inteiro {msgint}')