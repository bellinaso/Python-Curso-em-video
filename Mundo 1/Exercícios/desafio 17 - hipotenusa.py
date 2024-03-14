# importação da biblioteca
from math import hypot

# leitura dos valores
n1=float(input('Cateto oposto: '))
n2=float(input('Cateto adjacente: '))

# calculo
hi=hypot(n1, n2)

# resultado
print('A hipotenusa é {:.2f}'.format(hi))