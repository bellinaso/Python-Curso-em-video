print('Progressão aritimética 2.0')
print('==='*10)
n1=int(input('Digite o primeiro termo: '))
n2=int(input('Digite a razão: '))
pa=n1 # a progressão é igual ao primeiro termo
counter=0
while counter<10: # enquanto o contador for menor que 10 (10 termos de uma pa)
    pa+=n2 # (n1=n1+n2)
    counter+=1 # contador +1
    print(pa,end=' ')