print('print contando de trás pra frente')

for i in range(10,0,-1):
    print(i)

print('print pulando de dois ou mais')

for c in range(0,10,2):
    print(c)

print('print escrevendo um número e escrevendo cada vez maior')

n1=int(input('escreve um numero ae '))
for d in range(0,n1+1):
    print(d)

print('print somando todos números escritos')
y=0
for x in range(0,4):
    n1=int(input('Digite um valor: '))
    y+=n1
print(y)
