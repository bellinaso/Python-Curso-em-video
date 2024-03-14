num=(int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')))
print('Os valores digitados foram: ',end='')
for i in num:
    print(i,end=' ')
print(f'\nO valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ',end='')
for i in num:
    if i%2==0:
        print(i,end=' ')
# assisti a resolução
