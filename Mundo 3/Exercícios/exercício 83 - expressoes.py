pilha=[]
n1=str(input('Digite uma expressão matemática: '))
for i in n1:
    if i=='(':
        pilha.append('(') # se abrir parentese, adicionar '('
    elif i==')':
        if len(pilha)>0:
            pilha.pop() # se tiver ')' remover '('
        else:
            pilha.append(')')
            break
if len(pilha)==0: # quer dizer que pra cada parentese teve um par
    print('Sua expressão é válida.')
else:
    print('Sua expressão está errada.')
