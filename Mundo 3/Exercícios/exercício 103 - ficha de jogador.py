def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')

n1=str(input('Digite o nome do jogador: '))
n2=str(input('Digite o total de gols: '))
if n2.isnumeric():
    n2=int(n2)
else:
    n2=0
if n1.strip()=='':
    ficha(gols=n2)
else:
    ficha(n1,n2)
