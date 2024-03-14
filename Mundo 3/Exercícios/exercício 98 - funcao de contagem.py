from time import sleep

def linha():
    print('='*30)

def contador(lista):
    linha()
    print(f'\nContagem de {lista[0]} até {lista[1]-lista[2]} pulando {abs(lista[2])}.')
    for i in range(lista[0],lista[1],lista[2]):
        print(i,end=' ',flush=True)
        sleep(0.4)
    print('Fim!')

linha()
print('Contagem de 1 a 10 pulanto 1.')
for i in range(1,11,1):
    print(i,end=' ',flush=True)
    sleep(0.4)
print('Fim!\n')

linha()
print('Contagem de 10 a 0 pulando 2.')
for i in range(10,0,-2):
    print(i,end=' ',flush=True)
    sleep(0.4)
print('Fim!\n')

linha()
lista=[]
lista.append(int(input('Digite o início: ')))
lista.append(int(input('Digite o final: ')))
lista.append(int(input('Digite os passos: ')))
if lista[2]<0:
    lista[2]*=-1
if lista[2]==0:
    lista[2]=1 # se passos = 0 na verdade passos=1
if lista[1]<lista[2]:
    lista[1]-=1 # se final for < que passos = final - 1
    if lista[2]>0:
        lista[2]*=-1 # se passos for maior que 0 = passos = negativo
else:
    lista[1]+=lista[2] # caso passos não for > final, final + 1
if lista[1]<lista[0] and lista[1]>0:
    lista[2]*=-1
    lista[1]+=lista[2]
    # lista[0]-=lista[2]
contador(lista)
# ta funcionando, eu não vou tentar entender