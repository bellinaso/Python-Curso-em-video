dados=[]
pessoas=[]
for i in range(3):
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Digite a idade: ')))
    pessoas.append(dados[:])
    dados.clear()
for c in pessoas:
    print(f'{c[0]} tem {c[1]} anos.')
for c in pessoas:
    if c[1]>=21:
        print(f'{c[0]} é maior de idade.')
    else:
        print(f'{c[0]} é menor de idade.')
