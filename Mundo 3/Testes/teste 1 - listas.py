# variavel composta (tuplas)

# tuplas são imutaveis (não pode mudar nada)

teste='comida', 'tudo', 'até sua mãe', 'pizza', '24'
print(teste[-1]) 
print(teste[0])
print(teste[0:])
print(teste[1:4])
print(teste[:4])
print(teste[-5:])
print(sorted(teste)) # ordenado
print(teste.count('comida'))
print(f'Nesta tupla tem {len(teste)} elementos')

print('')
print('{}Área de testes{}'.format('\033[31m','\033[37m'))

print('')
for i in teste:
    print(f'Vou comer {i}')

print('')
for cont in range(0,len(teste)):
    print(f'Eu vou comer {teste[cont]} em {cont+1}° lugar')

print('')
for i, cont in enumerate(teste):
    print(f'Vou comer {cont} em {i+1}° lugar')