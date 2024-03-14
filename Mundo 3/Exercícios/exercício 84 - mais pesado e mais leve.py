temp=[]
dados=[]
maior=menor=0
while True:
    opç=' '
    temp.append(str(input('Nome: ').capitalize()))
    temp.append(int(input('Peso em Kg: ')))
    if len(dados)==0: # se não tiver nada em dados, maior e menor...
        maior=menor=temp[1]
    else:
        if temp[1]>maior:
            maior=temp[1]
        if temp[1]<menor:
            menor=temp[1]
    dados.append(temp[:])
    temp.clear()
    while opç not in 'sn':
        opç=str(input('Deseja adicionar mais uma pessoa? [s/n]').lower())
    if opç=='n':
        break
print('=-'*20)
print(f'Ao todo foram cadasrtadas {len(dados)} pessoas.')
print(f'O maior peso registrado foi {maior}Kg. As seguintes pessoas foram registradas com este peso: ',end='')
for i in dados:
    if i[1]==maior:
        print(f'{i[0]}',end=' ')
print(f'\nO menor peso registrado foi {menor}Kg. As seguintes pessoas foram registradas com este peso: ',end='')
for i in dados:
    if i[1]==menor:
        print(f'{i[0]}',end=' ')
# assisti a resolução