ficha=[]
while True:
    nome=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    média=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],média])
    opç=str(input('Deseja adicionar mais um aluno? [s/n] ').lower())
    if opç in 'n':
        break
print('+-'*20)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('_'*20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('+-'*20)
    opç=-1
    opç=int(input('Deseja ver a ficha de qual aluno? (0 para parar) '))
    if opç==0:
        break
    if opç<=len(ficha):
        print(f'Notas de {ficha[opç-1][0]} são {ficha[opç-1][1]}')
    else:
        print('Opção inválida.')