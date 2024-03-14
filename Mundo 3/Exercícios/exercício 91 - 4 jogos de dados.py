from random import randint
from time import sleep
from operator import itemgetter
jogos={
    'jogador 1':randint(1,6),
    'jogador 2':randint(1,6),
    'jogador 3':randint(1,6),
    'jogador 4':randint(1,6),
}
ranking=sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i,j in enumerate(ranking):
    print(f'O dado do {j[0]} caiu {j[1]} em {i+1}° lugar!')
    sleep(1)
    # tem que fazer o sort (ver a resolução)