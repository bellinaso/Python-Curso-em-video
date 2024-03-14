estado={}
brasil=[]
for c in range(3):
    estado['UF']=str(input('Digite o nome da unidade federativa: '))
    estado['Sigla']=str(input('Digite a sigla desta unidade federativa: '))
    brasil.append(estado.copy)
for e in estado:
    print(e)

'''filme={
    'título':'Star Guerra',
    'ano':1912,
    'diretor':'Mc Lã'
}
filme['ano']=1977
filme['tags']='sei la nave tiro exploração'

filme_1={
    'título':'matrix 0101001',
    'ano':4957,
    'diretor':'Donald trump'
}
filme_2={
    'título':'esqueci',
    'ano':1,
    'diretor':'bolsonaro 2022'
}
print(filme.keys())
print(filme.values())
print(filme.items())
print('=-'*15) # /////
for key,val in filme.items():
    print(f'O {key} é {val}')
print('=-'*15) # /////
locadora=[filme,filme_1,filme_2]
print(locadora[0]['ano'])
print(locadora[2]['título'])'''
