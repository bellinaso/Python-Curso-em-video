lista=[]
while True:
    n1=int(input('Digite um valor: '))
    lista.append(n1)
    while True:
        opc=str(input('Você deseja adicionar mais um valor? [s/n] ').lower())
        if opc in 'sn':
            break
        else:
            print('Opção inválida!')
    if 'n' in opc:
        break
par=[]
impar=[]
for i in lista:
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)
print(f'Os valores digitados foram: {lista}')
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')
