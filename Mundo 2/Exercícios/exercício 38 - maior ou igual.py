print('{}Digite dois números'.format('\033[32m'))
n1=int(input('Primeiro número: {}'.format('\033[33m')))
n2=int(input('{}Segundo número: {}'.format('\033[32m','\033[33m')))
if n1>n2:
    print('{}O primeiro valor é maior.'.format('\033[34m'))
elif n2>n1:
    print('{}O segundo valor é maior.'.format('\033[34m'))
elif n1==n2:
    print('{}Os dois valores "{}" são iguais.'.format('\033[34m',n1))
