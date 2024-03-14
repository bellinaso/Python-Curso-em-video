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
print('='*50)
for c in info:
    print(f'{c}: {info[c]}')
print('='*50)
print(f'O jogador jogou {n1} partidas no total.')
for i in range(n1):
    print(f'Na {i+1}ª foram feitos {info["Gols"][i]} gols.')