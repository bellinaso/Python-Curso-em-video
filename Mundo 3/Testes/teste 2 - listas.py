# variavel.append('item') adiciona um item na lista
# variavel.insert(0,'item') adiciona um item na posição 0
# del variavel[3] remove o item
# variavel.pop(3) também remove
# variavel.remove('valor do item') remove certo valor
num=[2,3,5,4,7,9]
#num[3]=3
num.append(99)
num.insert(3,0)
print(num)
num.sort(reverse=True)
for i in range(5):
    num.append(int(input('Digite um número ')))
if 12 in num:
    num.remove(12)
else:
    print('Tem 12 ai não o bobão')
for i,c in enumerate(num):
    print(c,end=' ')
    print(f'é o elemento {i+1} da lista')