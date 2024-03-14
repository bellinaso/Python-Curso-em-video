idades=média=velho=0
nomevelho=''
velhas=0
for i in range(1,5):
    print('----- {}ª PESSOA -----'.format(i)) #só pra ficar bonito
    n1=str(input('Nome: ').capitalize().strip()) 
    n2=int(input('Idade: '))
    n3=str(input('Sexo [M/F]: ').strip().lower())
    idades+=n2
    if velho==1 and n3=='m':
        velho=n2
        nomevelho=n1
    else:
        if n2>velho and n3=='m':
            velho=n2
            nomevelho=n1
    if n2<20 and n3=='f':
        velhas+=1
média=idades/4
print('A média de idades do grupo é de {} anos.'.format(média))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho,velho))
print('O total de muheres menores de 20 é de {}.'.format(velhas))
