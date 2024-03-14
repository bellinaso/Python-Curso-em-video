x=0
y=0
for n1 in range(1,501):
    if n1%3==0:
        if n1%2!=0:
            x+=n1
            y+=1
print('A soma de todos valores múltiplos de 3 e ímpares é igual a {}'.format(x))
print('A quantia de números somados foi de {}'.format(y))
