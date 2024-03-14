soma=cont=final=0
final=int(input('Digite um número: '))
while final!=999:
    soma+=final
    cont+=1
    final=int(input('Digite um número: '))
print('''Você acertou o número em {} tentativas.
A soma de todos números digitados foi {}'''.format(cont,soma))
