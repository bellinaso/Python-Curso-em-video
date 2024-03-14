n1=[[0,0,0],[0,0,0],[0,0,0]]
soma=soma_2=maior=0
for l in range(3):
    for c in range(3):
        n1[l][c]=int(input(f'Digite um valor para a posição {l+1}, {c+1}: '))
print('=-'*20)
for l in range(3):
    for c in range(3):
        print(f'[{n1[l][c]:^5}]',end='')
        if n1[l][c]%2==0:
            soma+=n1[l][c]
    print()
print(f'A soma dos valores pares é: {soma}')
for l in range(3):
    soma_2+=n1[l][2]
print(f'A soma dos valores da terceira coluna é: {soma_2}')
for c in n1[1]:
    if c>maior:
        maior=c
print(f'O maior número da segunda linha foi: {maior}')