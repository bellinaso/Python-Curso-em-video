print('     Sequência de Fibonacci')
print('---'*10)
n1=int(input('Quantos termos da sequência você quer mostrar? '))
num1=0
num2=1
print('---'*10)
print('{} > {}'.format(num1,num2),end='')
count=3
while count<=n1: # enquanto contagem for menor que termos:
    num3=num1+num2 # o terceiro termo é a soma dos dois últimos
    print(' > {}'.format(num3))
    num1=num2
    num2=num3 # faz com que num1 e num2 passem adiante
    # ex: 0 - 1 - 1 - 2
    #     n1 - n2 ->>>
    count+=1
print(' > Fim')
print('---'*10)