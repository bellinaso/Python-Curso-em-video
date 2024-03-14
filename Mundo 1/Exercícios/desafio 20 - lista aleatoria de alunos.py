from random import shuffle
print('Digite o número de quatro alunos para sortear uma ordem: ')
n1=str(input('Primeiro aluno: '))
n2=str(input('Segundo aluno: '))
n3=str(input('Terceiro aluno: '))
n4=str(input('Quarto aluno: '))
lista=[n1, n2, n3, n4]
shuffle(lista)
print('A ordem dos alunos é:')
print(lista)