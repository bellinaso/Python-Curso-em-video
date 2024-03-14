n1=int(input('Digite um número 0 a 9999: '))
u=n1//1%10
d=n1//10%10
c=n1//100%10
m=n1//1000%100
print('Unidade: {}'.format(u))
print('Desena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
