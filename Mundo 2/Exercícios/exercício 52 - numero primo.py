n1=(int(input('Digite um número: ')))
n2=0
for i in range(1,n1+1,1):
    if n1%i==0:
        print('\033[32m',end='')
        n2+=1
    else:
        print('\033[31m',end='')
    print('{} '.format(i),end='')
print('{}O número {} foi dividído {} vezes.'.format('\033[m',n1,n2))
if n2==2:
    print('{} é um número primo!'.format(n1))
else:
    print('{} não é um número primo'.format(n1))
#assisti resolução