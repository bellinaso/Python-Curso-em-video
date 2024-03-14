from time import sleep
print('{}Olá! Então você quer fazer um empréstimo para comprar uma casa?'.format('\033[32m'))
sleep(1)
print('{}==='.format('\033[31m')*10)
sleep(0.5)
print('{}Vamos começar com algumas perguntas.'.format('\033[36m'))
casa=int(input('{}Qual o preço da casa? R$'.format('\033[34m')))
print('{}==='.format('\033[31m')*10)
salario=(int(input('{}Qual o valor do seu salário atual? R$'.format('\033[34m'))))
print('{}==='.format('\033[31m')*10)
anos=(int(input('{}Em quantos anos você decide pagar a casa? '.format('\033[34m'))))
print('{}==='.format('\033[31m')*10)
print('{}Calculando...'.format('\033[34m'))
sleep(0.25)
# região dos if's e elif's
prestação=casa/(anos*12)
if prestação<=(salario*30)/100:
    print('{}Parabéns! Você poderá fazer seu empréstimo e comprar sua casa.'.format('\033[32m'))
    print('Sua prestação será de R${:.2f} reais.'.format(prestação))
else:
    print('{}Desculpa. Seu salário não permite que você faça o empréstimo.'.format('\033[31m'))
