from time import sleep
print('{}Calculadora simples'.format('\033[32m'))
print('{}==='.format('\033[37m')*10)
n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
opção=''
while opção!='5' and opção!='sair':
    print('{}==='.format('\033[37m')*10)
    print('''{}   Menu da calculadora   
    
    [1] Somar números.
    [2] Multiplicar números.
    [3] Maior número escolhido.
    [4] Escolher novos números.
    [5] Sair
    '''.format('\033[37m'))
    opção=str(input('Escolha o que deseja fazer >>>>> ').lower().strip())
    print('==='*10)
    if opção=='1' or opção=='somar números':
        print('A soma de {}+{} resulta em {}.'.format(n1,n2,n1+n2))
    elif opção=='2' or opção=='multiplicar números':
        print('A multiplicação de {}x{} resulta em {}.'.format(n1,n2,n1*n2))
    elif opção=='3' or opção=='maior número':
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('O maior número é {}.'.format(maior))
    elif opção=='4' or opção=='novos números':
        n1=int(input('Digite o primeiro valor: '))
        n2=int(input('Digite o segundo valor: '))
    elif opção=='5' or opção=='sair':
        print('Saindo...')
    else:
        print('{}Operação inválida. Tente novamente.'.format('\033[31m'))
    sleep(1)
print('See you next time :)')
