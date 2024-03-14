lista=[]
for i in range(5):
    n1=int(input('Digite um número: '))
    if i==0 or n1>lista[-1]: # se a posição for 0 ou n1 for menor que o último da lista
        lista.append(n1) # adicionar n1
        print('Adicionado no final da lista.')
    else:
        pos=0
        while pos<len(lista): # enquanto a posição for menor que a contagem da lista
            if n1<=lista[pos]: # se n1 for menor ou igual a posição
                lista.insert(pos,n1) # adicionar n1 na posição
                print(f'Adicionado na posição {pos}')
                break
            pos+=1
print('='*30)
print(f'Os valores foram digitados em ordem, porém sem utilizar o comando lista.sort()\nLista: {lista}')
# assisti resolução