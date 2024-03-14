lista=[]
while True:
    info={
        'Nome':'',
        'Gols':[],
        'Gols totais':0
    }
    info['Nome']=str(input('Digite o nome do jogador: ').title().strip())
    n1=int(input('Digite o total de jogos jogados: '))
    for i in range(n1):
        info['Gols'].append(int(input(f'Quantos gols foram feitos no jogo {i+1}? ')))
        info['Gols totais']+=info['Gols'][i]
    while True:
        opç=str(input('Deseja adicionar mais um jogador? [s/n] '))
        if opç in 'sn':
            break
    lista.append(info.copy())
    if opç in 'n':
        break
print('='*50)
print(f'{"N°":<4}{"NOME":<10}{"GOLS TOTAIS":>12}')
for i,p in enumerate(lista):
    print(f'{i+1:<4}{p["Nome"]:<10}{p["Gols totais"]:>8}')
print('='*30)
while True:
    opç=-1
    opç=int(input('Qual jogador deseja ver as informações? (0 para parar) '))
    print(f'-> Mostrando as informações do jogador {lista[opç-1]["Nome"]}')
    if opç==0:
            break
    if opç<=len(lista):
        for c in range(len(lista)):
            print(f'No jogo {c+1} foram feitos {lista[opç-1]["Gols"][c]}')
    else:
        print('Opção inválida.')
        
# deu erro depois de dar certo DESISTO