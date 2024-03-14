x=('{}==='.format('\033[35m')*10)
print(x)
print('   Os 10 termos de uma PA')
print(x)
n1=int(input('Digite um termo: '))
n2=int(input('Digite a razão: '))
decimo=n1+(10-1)*n2
for i in range(n1,decimo+n2,n2):
    print('{}{} '.format('\033[32m',i),end='> ')
print('Acabou')
# assisti resolução