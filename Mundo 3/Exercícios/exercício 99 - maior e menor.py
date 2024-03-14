from time import sleep

def maior_num(maior):
    maior=0
    for i in lista:
        if maior==0:
            maior=i
        else:
            if i>maior:
                maior=i
    print(f'Analisando os valores {lista}.')
    sleep(2)
    print(f'O maior valor é {maior}.')
    print('='*50)

maior=0
lista=[]
for i in range(10):
    lista.append(int(input(f'Digite o {i+1}° número: ')))
maior_num(maior)

lista=[]
for i in range(5,0,-1):
    lista.append(int(input(f'Digite mais {i} valores: ')))
maior_num(maior)