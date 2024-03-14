n1=n2=0
name=str(input('Digite seu nome: '))
years=int(input('Digite sua idade: '))
if years <12:
    print(f'Sua idade é {years}? Lamento {name} mas você é muito novo para nosso programa.')
else:
    print(f'Olá {name}!')
    print('-'*30)
    while True:
        n1=int(input('Digite um número: (999 para parar) '))
        if n1==999:
            break
        n2+=n1
    # print('Aqui acaou e a soma de todos números foi {}'.format(n2))
    print(f'A soma de todos os números foi {n2}') # f string

# provavelmente um dos exercícios 
print('{}Área de testes'.format('\033[32m'))
print(f'O {name:=^20} se chama {name:=<20} pq seu nome é {name}') #formatações