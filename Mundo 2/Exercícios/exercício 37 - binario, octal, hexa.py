n1=int(input('{}Digite um número qualquer: '.format('\033[32m')))
print('{}Escolha em qual língua será traduzido:{}\n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal'.format('\033[31m','\033[33m'))
n2=int(input('---> {}'.format('\033[36m')))
if n2==1:
    print('{}Em Binário, {} é representado como: {}'.format('\033[32m',n1,bin(n1)[2::]))
elif n2==2:
    print('{}Em Octal, {} será representado como: {}'.format('\033[32m',n1,oct(n1)[2::]))
elif n2==3:
    print('{}Em Exadecimal, {} é mostrado como: {}'.format('\033[32m',n1,hex(n1)[2::]))
