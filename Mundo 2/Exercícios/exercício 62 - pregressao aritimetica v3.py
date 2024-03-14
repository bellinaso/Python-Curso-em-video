print('Progressão aritimética 2.0')
print('==='*10)
n1=int(input('Digite o primeiro termo: '))
n2=int(input('Digite a razão: '))
opção=''
pa=n1
total=0
termo=10
while termo!=0:
    counter=0
    total+=termo
    print('A progressão aritimética do termo {} com a razão {} é: '.format(n1,n2))
    while counter<termo:
        print(pa,end=' > ')
        pa+=n2
        counter+=1
    print('')
    termo=int(input('Quantos temos a mais deseja mostrar? '))
print('A progressão foi finalizada com {} termos mostrados.'.format(total))
