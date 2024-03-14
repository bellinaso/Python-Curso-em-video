n1=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(3):
    for c in range(3):
        n1[l][c]=int(input(f'Digite um valor para a posição {l+1}, {c+1}: '))
    # define cada número em cada linha e coluna
print('=-'*20)
for l in range(3):
    for c in range(3):
        print(f'[{n1[l][c]:^5}]',end='')
    print() # quando acaba uma linha ele pula
# assisti a resolução