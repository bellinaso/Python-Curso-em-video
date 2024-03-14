n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
n3=int(input('Digite mais um número: '))
# menor
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
#maior
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('')
print('O menor valor digitado foi: {}'.format(menor))
print('---'*10)
print('E o maior valor digitado foi: {}'.format(maior))
