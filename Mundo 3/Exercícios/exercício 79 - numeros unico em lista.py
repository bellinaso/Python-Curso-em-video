num=[]
while True:
    n1=int(input('Digite um número: '))
    if n1 in num:
        print('Número repetido, não será adicionado.')
    else:
        num.append(n1)
    n2=str(input('Deseja adicionar mais números? [s/n] ').lower())
    if n2=='n':
        break
print('Você digitou os valores: {}'.format('\033[32m'),end='')
num.sort()
for i in num:
    print(i,end=' ')