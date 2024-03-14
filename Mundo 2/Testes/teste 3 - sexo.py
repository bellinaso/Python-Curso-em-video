r='m','f'
while r != 'm' and r != 'f':
    r=str(input('Digite seu sexo [M/F]: ').lower())
if r == 'm':
    r='masculino'
else:
    r='feminino'
print('Seu sexo é {}.'.format(r))
# igual o exerciocio 56 