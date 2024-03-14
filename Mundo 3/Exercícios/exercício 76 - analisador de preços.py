conta='Pastel de flango',2.50,'3 Cadernos',30.00,'Cadeira',500.00
print('/='*25)
print('Conta final de compras'.center(50))
print('\='*25)
for i in range(0,len(conta)):
    if i %2==0:
        print(f'{conta[i]:.<40}',end='')
    else:
        print(f'R${conta[i]:>5.2f}')
