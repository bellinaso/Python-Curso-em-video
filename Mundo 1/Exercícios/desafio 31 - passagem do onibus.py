n1=int(input('Qual distância da sua viagem em Km? '))
if n1<=200:
    print('O valor final da viagem foi de R${:.2f}'.format(n1*0.50))
else:
    print('O valor final da viagem foi de R${:.2f}'.format(n1*0.45))
