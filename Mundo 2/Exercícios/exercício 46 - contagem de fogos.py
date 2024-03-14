from time import sleep
n1=input('{}Pressione a tecla {}enter{} para iniciar a contagem do show de fogos. \n'.format('\033[31m','\033[30;41m','\033[31;40m'))
print('{}   Contagem iniciando em     '.format('\033[30;43m'))
for n2 in range(3,0,-1):
    print('        {}                    '.format(n2))
    sleep(1)
print('{}   !!Contagem iniciada!!     '.format('\033[30;41m'))
for n3 in range(10,0,-1):
    if n3==10:
        print('        10                   ')
        sleep(1)
    print('        {}                    '.format(n3-1))
    sleep(1)
print('    Fogos sendo lançados     '.format('\033[30;43m'))
