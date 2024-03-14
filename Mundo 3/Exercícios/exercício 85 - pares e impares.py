num=[[],[]]
num_1=0
for i in range(7):
    num_1=(int(input('Digite um número: ')))
    if num_1%2==0:
        num[0].append(num_1)
    else:
        num[1].append(num_1)
num[0].sort
num[1].sort
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
