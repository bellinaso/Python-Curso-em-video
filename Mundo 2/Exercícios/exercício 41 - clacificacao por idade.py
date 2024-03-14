from datetime import date
n1=str(input('{}Digite sua dada te nascimento como demonstrado abaixo. {}\nXX/XX/XXXX: '.format('\033[31m','\033[32m')).replace('/',' ').strip())
print('{}==='.format('\033[36m')*12)
x=n1.split()
data=date.today()
ano=data.year
n2=int(x[2])
# print(ano-n2)
if (ano-n2)<=9:
    print('{}Sua categoria na Confederação Nacional de Natação é {}mirim.'.format('\033[32m','\033[4;36m')) #2012
elif (ano-n2)<=14:
    print('{}Sua categoria na Confederação Nacional de Natação é {}infantil.'.format('\033[32m','\033[4;36m')) #2007
elif (ano-n2)<=19:
    print('{}Sua categoria na Confederação Nacional de Natação é {}junior'.format('\033[32m','\033[4;36m')) #2002
elif (ano-n2)<=25:
    print('{}Sua categoria na Confederação Nacional de Natação é {}sênior.'.format('\033[32m','\033[4;36m')) #2001
elif (ano-n2)>20:
    print('{}Sua categoria na Confederação Nacional de Natação é {}master'.format('\033[32m','\033[4;36m')) #>2001

#informações
# 9 anos mirim
# 14 anos infantil
# 19 anos junior
# 20 anos sênior
# acima master
