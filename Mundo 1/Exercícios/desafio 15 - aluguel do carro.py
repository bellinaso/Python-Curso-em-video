n1=int(input('Quantos dias você ficou com o carro? '))
n2=float(input('Quantos quilômetros foram rodados com o carro neste período? '))
n3=(n1*60)+(n2*0.15)
print('O total a pagar é de R${}'.format(n3))
