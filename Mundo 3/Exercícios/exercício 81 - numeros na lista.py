lista=[]
while True:
    n1=int(input('Digite um valor: '))
    lista.append(n1)
    while True:
        opc=str(input('Você deseja adicionar mais um número? [s/n] ').lower())
        if opc not in 'sn':
            print('Opção inválida!')
        else:
            break
    if opc in 'n':
        break

lista.sort(reverse=True)

print('='*20)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não está na lista.')
