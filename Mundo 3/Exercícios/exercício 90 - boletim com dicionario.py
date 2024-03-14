média=0
aluno={
    'nome':'',
    'média':[],
    'status':''
}
aluno['nome']=str(input('Digite o nome do aluno: ').capitalize())
for i in range(3):
    aluno['média'].append(int(input(f'Digite a {i+1}ª média: ')))
    média+=aluno['média'][i]
print(f'{"NOME":<10}{"MÉDIA":>8}')
print('━'*20)
print(f'{aluno["nome"]:<10}{média/3:>8.1f}')
print('━'*20)