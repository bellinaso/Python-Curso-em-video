def notas(num=[],situação=False):
    soma=0
    aluno={}
    aluno['total']=len(num)
    aluno['maior']=max(num)
    aluno['menor']=min(num)
    for i in num:
        soma+=i
    aluno['média']=soma/len(num)
    if situação:
        if aluno['média']>9:
            situação='MUITO BOA'
        elif aluno['média']>=7 and aluno['média']<9:
            situação='BOA'
        elif aluno['média']>=5 and aluno['média']<7:
            situação='RUIM'
        elif aluno['média']>=3 and aluno['média']<5:
            situação='MUITO RUIM'
        aluno['situação']=situação
    return aluno.values()

situação=False
nome=str(input('Digite seu nome: ').title())
print('Digite as notas')
valores=[]
while True:
    while True:
        n1=str(input('Nota: '))
        if n1.isnumeric():
            n1=int(n1)
            valores.append(n1)
            break
        else:
            print('Nota inválida! Tente novamente.')
    opç=str(input('Deseja adicionar mais uma nota? [s/n] ').strip().lower())
    if opç in 'n':
        break
n1=str(input('Deseja ver a situação do aluno? [s/n] ').strip().lower())
if n1 in 's':
    situação=True
#print(notas(valores,situação))
print(f'{"NOME":<16}{"NOTAS TOTAIS":<16}{"MAIOR NOTA":<16}{"MENOR NOTA":<16}{"MÉDIA":<16}',end='')
if situação:
    print(f'{"SITUAÇÃO":<16}')
    print('━'*90)
else:
    print()
    print('━'*70)
print(f'{nome:<16}',end='')
for c,i in enumerate(notas(valores,situação)):
    if c==3:
        print(f'{i:<16.1f}',end='')
    else:
        print(f'{i:<16}',end='')
