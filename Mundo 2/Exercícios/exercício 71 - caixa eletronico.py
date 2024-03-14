from time import sleep
print('='*30)
print('{:^30}'.format('BamCO iMter'))
print('='*30)
n1=int(input('Qual valor você quer sacar? R$'))
total=n1
nota=50
notas=0
print('='*30)
print('Transação pendente. Aguarde!')
print('='*30)
sleep(1)
print('Saque concluído!')
while True:
    if total>=nota: 
        total-=nota
        notas+=1 # se o montante for maior que a maior nota, retira o valor da maior nota o máximo possível
    else: # caso não de mais pra tirar a maior nota, ele tenta tirar uma mais leve
        if notas>0: # se o montante estiver completo ele printa os valores
            print(f'Total de {notas} notas de R${nota}')
            sleep(0.2)
        if  nota==50: 
            nota=20
        elif nota==20:
            nota=10
        elif nota==10:
            nota=5
        elif nota==5:
            nota=2
        elif nota==2:
            nota=1
        notas=0
        if total==0:
            break
print('='*30)
# assisti a resolução
