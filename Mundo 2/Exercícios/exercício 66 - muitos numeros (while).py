n1=n2=counter=0
while True:
    n1=int(input('Digite um número: (999 para parar) '))
    if n1==999:
        break
    n2+=n1
    counter+=1
# print('Aqui acaou e a soma de todos números foi {}'.format(n2))
print(f'A soma de todos os {counter} números foi {n2}') # f string