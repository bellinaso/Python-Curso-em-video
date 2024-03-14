média=maior=menor=cont=soma=0
opção=''
while opção in 'Ss':
    n1=int(input('Digite um número: '))
    cont+=1
    soma+=n1
    if cont==1: # 1 define qual é o maior
        maior=menor=n1
    else: # 2 compara o maior com o menor
        if n1>maior:
            maior=n1
        if n1<menor:
            menor=n1 
    opção=str(input('Você deseja escrever mais um número? [s/n] '))
média=soma/cont
print('''O maior número foi {}
O menor número foi {}
A média de todos números foi {}'''.format(maior, menor, média))