print('{}Sua média será avaliada.'.format('\033[36m'))
print('{}==='.format('\033[31m')*10)
n1=int(input('{}Digite a nota do primeiro trimestre: {}'.format('\033[34m','\033[32m')))
n2=int(input('{}Digite a nota do segundo trimestre: {}'.format('\033[34m','\033[32m')))
n3=int(input('{}Digite a nota do terceiro trimestre: {}'.format('\033[34m','\033[32m')))
x=(n1+n2+n3)/3
if x<5:
    print('{}Sua nota foi de {}{:.2f}{}, e não foi o suficiente para a sua aprovação. Você está reprovado.'.format('\033[31m','\033[4m',x,'\033[0;31m'))
elif x>5 and x<6.9:
    print('{}Sua nota resultou em {}{:.2f}{}, e você entrou em recuperação.'.format('\033[33m','\033[4;31m',x,'\033[0;33m'))
elif x>7:
    print('{}Parabéns! Sua média foi de {}{:.2f}{}. Você está aprovado!'.format('\033[32m','\033[4;31m',x,'\033[0;32m'))
