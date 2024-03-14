from time import sleep
from random import randint

def sorteio():
    """
    > Servira para sortear 5 valores entre 1 e 10, e adicionalos em uma lista"""
    for i in range(5):
        lista.append(randint(1,10))
    print('Sorteando valores...', end=' ')
    for n in lista:
        print(n, end=' ',flush=True)
        sleep(0.7)

def soma(pares):
    for n in lista:
        if n%2==0:
            pares+=n
    print(f'\nA soma dos pares sorteados é: {pares}')


lista=[]
pares=0
sorteio()
soma(pares)