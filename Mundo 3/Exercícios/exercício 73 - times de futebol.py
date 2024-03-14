times='Atlético MG','Palmeiras','Flamengo','Fortaleza','Bragantino','Internacional','Corinthians','Fluminense','Athletico PR','Cuiabá','Atlético GO','São Paulo','Ceará SC','Santos','Bahia','Juventude','América MG','Grêmio','Sport Recife','Chapecoense'
print('{}Os 5 primeiros times foram:{}'.format('\033[32m','\033[37m'))
for i, c in enumerate(times[0:5]):
    print(f'{c} em {i+1}° lugar',end=' -> ')

print('\n')
print('{}Os últimos 4 times da lista foram:{}'.format('\033[32m','\033[37m'))
for c in range(15,20):
    print(f'{times[c]} em {c+1}° lugar',end=' -> ')

print('\n')
print('{}Os times em ordem alfabéticas são:{}'.format('\033[32m','\033[37m'))
for i in sorted(times):
    print(f'{i}',end=', ')

print('\n{}O time Chapecoense ficou em: {}{}° lugar'.format('\033[32m','\033[37m',times.index('Chapecoense')+1))
