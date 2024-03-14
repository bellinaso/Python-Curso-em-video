'''numero = int(input("Fatorial de: ") )

resultado=1
for n in range(1,numero+1):
    resultado *= n

print(resultado)'''

n1=int(input('Digite um número: '))
fator=1
for i in range(n1,0,-1): # vai de 1 até n1 somando 1
    print('{}'.format(i), end='')
    print('x' if i>1 else '=',end='')
    fator*=i # fator=fator.contagem
    i-=1
print('{}'.format(fator))