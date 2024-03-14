n1=int(input('Qual foi a velocidade atingida?\n(Digite apenas o número) '))
n2=(n1-80)*7
if n1>=80:
    print('Você foi multado e deverá pagar R${:.2f}!'.format(n2))
else:
    print('Você está dentro do limite.')
