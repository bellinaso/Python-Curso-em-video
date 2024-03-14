'''numero = int(input("Fatorial de: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)'''

n1=int(input('Digite um número: '))
fator=1
count=n1
while count>0: # enquanto contagem for menor ou igual que numero...
    print('{}'.format(count), end='')
    print('x' if count>1 else '=',end='')
    fator*=count # fator.fator.contagem
    count-=1 # contagem - 1
print('{}'.format(fator))