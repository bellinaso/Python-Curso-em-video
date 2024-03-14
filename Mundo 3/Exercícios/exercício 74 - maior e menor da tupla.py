from random import randint
maior=menor=cont=0
num=(randint(1,10),randint(1,10),randint(1,10),
randint(1,10),randint(1,10))
print('Os números sorteados foram: ',end=' ')
for i in num:
    print(i,end=' ')
print('')
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor foi {min(num)}') # max e min podem ser usados apenas em tuplas
# assisti a resolução
