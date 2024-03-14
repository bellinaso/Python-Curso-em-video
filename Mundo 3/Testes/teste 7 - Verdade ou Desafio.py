from random import choice

def colors(color=0):
        lista=[
        '\033[30m',
        '\033[31m',
        '\033[32m',
        '\033[33m',
        '\033[34m',
        '\033[35m',
        '\033[36m',
        '\033[37m'
        ]
        return lista[color]


players=[]
players_choice=[]
counting=1
while True:
    n1=str(input(f'{colors(2)}Digite o nome do {counting}° jogador: ').title())
    counting+=1
    if 'null' in n1.lower():
        break
    else:
        players.append(n1)

counting=0
while counting<2:
    n2=choice(players)
    if n2 not in players_choice:
        players_choice.append(n2)
        counting+=1
print(f'{colors(6)}{players_choice[0]}{colors(2)} pergunta para {colors(6)}{players_choice[1]}')