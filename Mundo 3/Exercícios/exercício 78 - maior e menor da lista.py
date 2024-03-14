lista=[]
maior=maiorpos=menor=menorpos=0
print('Digite 5 valores, e o programa mostrará qual o maior e o menor da lista.')
for i in range(5):
    lista.append(int(input(f'{i+1}° valor: ')))
    if maior==0:
        maior=lista[i]
        menor=lista[i]
    else:
        if lista[i]>maior:
            maior=lista[i]
            maiorpos=i
        if lista[i]<menor:
            menor=lista[i]
            menorpos=i
print(f'O maior número da lista foi {maior} na posição {maiorpos+1}\nE o menor foi {menor} na posição {menorpos+1}')
