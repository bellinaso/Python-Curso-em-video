def linha(size,color='\033[m'):
    '''Essa função cria uma linha de caractéres apenas para estética do script'''
    print(f'{color}='*size)


def cores(num):
    '''Essa função deverá ser usada em uma formatação de string, com números de 0 a 7 que definem cor'''
    lista=[
        '\033[30m',
        '\033[31m',
        '\033[32m',
        '\033[33m',
        '\033[34m',
        '\033[35m',
        '\033[36m',
        '\033[37m'
    ]
    try:
        return lista[num]
    except:
        print('''
        \033[30;43m utility.cores \033[40m
        \033[31mINDEX ERROR! Este número de cor é inválido, tente escolher entre 0 a 6 \033[m''')

def centralização(num,text):
    '''Esta função centraliza o texto enviado pela sintaxe Text e centraliza no tamanho do valor definido na sintaxe Num'''
    n1=(f'{text:^{num}}')
    try:
        print(n1)
        #return n1
    except:
        print('''
        \033[30;43m utility.centralização \033[40m
        \033[31mERRO! O valor digitado não é correspondido pelo sistema.\033[m''')