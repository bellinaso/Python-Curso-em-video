from random import randint
from time import sleep

print('='*30)
print(f'{"Jogo da mega sena":^30}')
print('='*30)

n1=int(input('Quantos jogos você quer sortear? '))
print(f'{f"Sorteando {n1} jogos":^30}')

for i in range(n1):
    jogos=[]
    cont=0

    while cont!=6:
        num=randint(1,60)
        if num not in jogos:
            jogos.append(num)
            cont+=1
            
    print(f'Jogo {i+1}: {jogos[:]}')
    sleep(0.3)
print(f'{"Boa sorte":^30}')
