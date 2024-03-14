from time import sleep
print('Digite três medidas de retas para calcular se será possível montar um triangulo: ')
print('')
n1=float(input('Primeira medida: '))
n2=float(input('Segunda medida: '))
n3=float(input('Terceira medida: '))
print('Calculando...')
sleep(0.50)
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('Será possível montar um triangulo!')
else:
    print('Não será possível montar um triangulo. Uma reta é maior que a soma das outras duas.')
