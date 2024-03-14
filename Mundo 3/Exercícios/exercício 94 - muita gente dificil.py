lista=[]
média=0
while True:
    pessoa={
        'nome':'',
        'sexo':'',
        'idade':0
    }
    pessoa['nome']=str(input('Digite o nome: ').title())
    while True:
        pessoa['sexo']=str(input('Digite o sexo: [M/F] ').lower().strip())[0]
        if pessoa['sexo'] in 'MmFf':
            break
    if pessoa['sexo'] in 'Mm':
        pessoa['sexo']='masculino'
    else:
        pessoa['sexo']='feminino'
    pessoa['idade']=int(input('Digite a idade: '))
    while True:
        opção=str(input('Deseja adicionar mais uma pessoa? [s/n] '))
        if opção not in 'sn':
            print('{}Opção inválida{}'.format('\033[31m','\033[37m'))
        if opção in 'sn':
            break
    lista.append(pessoa.copy())
    if opção in 'n':
        break
print('=-'*30)
print(lista)
print('=-'*30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print('=-'*30)
for i in lista:
    média+=i['idade']/(len(lista))
print(f'A média de idade do grupo é {média:.0f}.')
print('=-'*30)
print('As mulheres registradas foram: ',end='')
for p in lista:
    if p['sexo']=='feminino':
        print(f'{p["nome"]}',end=' ')
print('\nAs pessoas com idades registradas acima da média são: ',end='')
for p in lista:
    if p['idade']>média:
        print(f'{p["nome"]}',end=' ')
