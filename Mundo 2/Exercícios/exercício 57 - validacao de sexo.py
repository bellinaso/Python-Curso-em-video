r=str(input('Digite seu sexo [M/F] '))
while r not in 'MmFf':
    r=str(input('Sexo inválido. Digite novamente: '))
if r == 'm':
    r='masculino'
else:
    r='feminino'
print('==='*10)
print('Seu sexo é {}.'.format(r))
