num='zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
while True:
    n1=int(input('Digite um número de 0 a 20: '))
    if 0<=n1<21:
        break
    else:
        print('Este número é inválido.')
print(f'Você digitou o número {num[n1]}')