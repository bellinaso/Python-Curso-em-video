from random import randint

print('''┌────────────────────────────┐
│ Vamos jogar par ou ímpar?  │
└────────────────────────────┘''')
# ─┌┐└┘│
counter=0
while True:
    print('==='*10)
    n1=11
    while n1>10:
        n1=int(input('Digite um número até 10: '))
        if n1>10:
            print('Ops! Esse número é muito grande.\n')
    n2=' '
    while n2 not in 'PpIi':
        n2=str(input('Você deseja par ou ímpar? [p/i] '))
        if n2=='p':
            pc=1 #ímpar
        else:
            pc=2 #par
    random=randint(1,10)
    parimpar=n1+random
    if parimpar%2==0:
        num=2 # par
    else:
        num=1 # ímpar
    if n2 in 'p' and num==2:
        print(f'Parabén você venceu! O computador escolheu {random}')
        counter+=1
    elif n2 in 'i' and num==1:
        print(f'Parabéns você venceu! O computador escolheu {random}')
        counter+=1
    else:
        break
print(f'Você perdeu depois de {counter} virórias consecutivas :( o computador escolheu {random}')
