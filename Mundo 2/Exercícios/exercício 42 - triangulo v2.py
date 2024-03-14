print('{}Digite três medidas e o programa irá responder se é possível formar um triângulo, e qual seu tipo.'.format('\033[4;31m'))
n1=float(input('{}Primeira medida: '.format('\033[0;32m')))
n2=float(input('{}Segunda medida: '.format('\033[0;32m')))
n3=float(input('{}Terceira medida: '.format('\033[0;32m')))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('{}É possível montar um triângulo.'.format('\033[34m'))
    if n1==n2 and n2==n3:
        print('E seu tipo é equilátero')
    elif n1==n2 or n2==n3 or n3==n1:
        print('E seu tipo é isóceles.')
    elif n1!=n2 or n2!=n3 or n3!=n1:
        print('E seu tipo é escaleno. ')
else:
    print('{}Ops! Não é possível montar um triângulo! \nTente outras medidas.'.format('\033[31m'))
