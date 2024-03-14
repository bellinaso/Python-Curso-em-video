import random
nome1=str(input('Digite o número do primeiro aluno: '))
nome2=str(input('Digite o número do segundo aluno: '))
nome3=str(input('Digite o número do terceito aluno: '))
nome4=str(input('Digite o número do quarto aluno: '))
lista=(nome1,nome2,nome3,nome4)
escolha=random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolha))
