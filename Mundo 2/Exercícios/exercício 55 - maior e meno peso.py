maior=0
menor=0
for i in range(1,6):
    n1=float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if maior==0:
        maior=n1
        menor=n1
    else:
        if n1>maior:
            maior=n1
        if n1<menor:
            menor=n1
print('O maior peso foi {}Kg'.format(maior))
print('E o menor peso foi {}Kg'.format(menor))
# assisti a resolução
