x=0
y=0
for n1 in range(0,6):
    n2=int(input('Digite um número: '))
    if n2%2==0:
        x+=n2
        y+=1
print('A soma dos {} números somados é igual a: {}'.format(y,x))
